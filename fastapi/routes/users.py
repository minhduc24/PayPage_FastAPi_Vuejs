from fastapi import APIRouter, Depends
from requests import Session
from models.user import *
from db.database import SessionLocal


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/user/{user_id}")
async def get_user1(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    return user
   

@router.post("/create_user")
async def create_user(user: UsersModel, db: Session = Depends(get_db)):
    user = create_new_user(db, user)
    return user



