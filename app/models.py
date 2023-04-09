from pydantic import BaseModel
from .database import Base
from sqlalchemy import Column, String

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    

class UserUpdate(BaseModel):
    name: str
    email: str
    password: str
    

class User(Base):
    __tablename__ = "users"
    
    id = Column(primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)