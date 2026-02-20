from pydantic import BaseModel, EmailStr,Field

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=72)

class UserDelete(BaseModel):
    email: EmailStr
    id : int

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True

      