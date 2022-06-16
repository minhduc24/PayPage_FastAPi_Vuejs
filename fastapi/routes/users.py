from itertools import accumulate
from typing import Optional
from fastapi import APIRouter, Depends
from requests import Session
from models.user import *
from db.database import SessionLocal


router = APIRouter()

class User(BaseModel):
    user_name: str 
    user_img: str 
    accumulate_points: int 
    class Config:
        orm_mode = True
    
class UserUpdate(BaseModel):
    accumulate_points: Optional[int] = None
    class Config:
        orm_mode = True
        
        
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users/{user_id}")
async def get_user1(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    return user
   

@router.post("/users")
async def create_user(user: User, db: Session = Depends(get_db)):
    user1 = create_new_user(db, user)
    return user1


@router.delete("/users/{user_id}")
async def delete(user_id: int, db: Session = Depends(get_db)):
    user = delete_user(db, user_id)
    return user    

# @router.patch("/users/{user_id}", response_model=UserUpdate)
# async def update_item1(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
#     db_user = get_user(db, user_id)
#     user_data = user.dict(exclude_unset=True)
#     for key, value in user_data.items():
#         setattr(db_user, key, value)
#         print(11111111,user_data.items())
#     db.add(db_user)
#     db.commit()
#     return db_user

@router.patch("/users/{user_id}", response_model=UserUpdate)
async def update_item1(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = update_user(db, user_id, user)
    return db_user