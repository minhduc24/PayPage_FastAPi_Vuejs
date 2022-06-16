from email.policy import default
from sqlalchemy import Boolean, Column, Integer, String
from db.base_class import Base


def imgDefault():
    src = "https://www.kindpng.com/imgv/iwoxbb_user-profile-default-image-png-clipart-png-download/"
    return  src 


class User(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_name = Column(String,unique=True,nullable=False)
    user_img = Column(String, default=imgDefault())
    accumulate_points = Column(Integer, nullable= False)
    
