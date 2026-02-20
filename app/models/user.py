from sqlalchemy import Column, Integer, String,Boolean,text
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255))
    isActive = Column(Boolean, default=False,server_default=text("0"), nullable=False)
