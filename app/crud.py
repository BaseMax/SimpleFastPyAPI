from sqlalchemy.orm import Session
from . import models


def create_user(db: Session, user: models.UserCreate):
    
    db_user = models.User