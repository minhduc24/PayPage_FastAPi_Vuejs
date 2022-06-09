from email.policy import default
from sqlalchemy import Boolean, Column, Integer, String
from db.base_class import Base

class User(Base):
    
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String,unique=True,nullable=False)
    user_img = Column(String, default="https://www.kindpng.com/imgv/iwoxbb_user-profile-default-image-png-clipart-png-download/")
    accumulate_points = Column(Integer, nullable= False)
    
