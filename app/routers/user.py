from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from typing import List

from ..database import engine
from ..models import UserCreate, UserUpdate
from ..crud import create_user, get_user, update_user, elete_user


Base = declarative_base()

Base.metadata.create_all(bind=engine)

router = APIRouter()

