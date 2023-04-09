from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from typing import List

from ..database import engine, get_db
from ..models import UserCreate, UserUpdate
from ..crud import create_user, get_user, update_user, delete_user, get_users


router = APIRouter()

@router.get("/users")
async def get_all_users(db: Session = Depends(get_db)):
    return get_users(db=db)