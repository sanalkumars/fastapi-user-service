from fastapi import APIRouter, Depends, HTTPException,Response
from sqlalchemy.orm import Session
from app.schemas.user import  UserDelete,UserResponse
from app.api.deps import get_db
from app.models.user import User
from typing import List
from app.core.security import get_current_user


router = APIRouter(prefix="/user", tags=["user"])

@router.put('/delete')
def deleteUser(user: UserDelete, db : Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if not db_user.is_active:
        raise HTTPException(status_code=400, detail="User already deactivated")
    
    db_user.is_active = False
    db.commit()
    db.refresh(db_user)

    return { "message" : "User Deleted Successfulyy..."}


@router.get("/users", response_model=List[UserResponse])
def get_all_active_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    print("current user is ",current_user)
    return db.query(User).filter(User.is_active == True).all()