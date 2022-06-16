from sqlalchemy.orm import Session
from db.entities.user import User
from pydantic import BaseModel


    
def get_user(db: Session, user_id: int):
    result = db.query(User).filter(User.id == user_id).first()
    return result

def create_new_user(db: Session, user):
    userInstance = User(
        user_name = user.user_name, 
        user_img = user.user_img,   
        accumulate_points = user.accumulate_points
    )
    db.add(userInstance)
    db.commit()
    return {"ok": True}

# def update_user(db: Session, user_id: int)


def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()
    return {"ok": True}


def update_user(db: Session, user_id: int, user):
    db_user = db.get(User, user_id)
    user_data = user.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(db_user, key, value)
    db.add(db_user)
    db.commit()
    return db_user


# def update_user(db: Session, user_id: int, user):
#     db_user = db.get(User, user_id)
#     user_data = user.dict(exclude_unset=True)
#     for key, value in user_data.items():
#         setattr(db_user, key, value)
#     db.add(db_user)
#     db.commit()
#     return db_user


# @router.patch("/users/{user_id}", response_model=UserUpdate)
# async def update_item1(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
#     db_user = update_user(db, user_id, user)
#     return db_user