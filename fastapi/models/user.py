from sqlalchemy.orm import Session
from db.entities.user import User
from pydantic import BaseModel


class UsersModel(BaseModel):
    id: int 
    user_name: str
    user_img: str 
    accumulate_points: int     
    
    
    
def get_user(db: Session, user_id: int):
    result = db.query(User).filter(User.id == user_id).first()
    return result

def create_new_user(db: Session, user: UsersModel):
    user = User(
        id = user.id,
        user_name = user.user_name, 
        user_img = user.user_img,   
        accumulate_points = user.accumulate_points
    )
    result = db.add(user)
    db.commit()
    db.refresh(user)
    return result
