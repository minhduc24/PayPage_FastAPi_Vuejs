from sqlalchemy import Boolean, Column, Integer, String, DateTime
from db.base_class import Base

class Order(Base):
   
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable= False)
    created_at = Column(DateTime, nullable= False)
    
