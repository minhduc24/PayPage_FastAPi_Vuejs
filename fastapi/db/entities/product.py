from sqlalchemy import Boolean, Column, Integer, String
from db.base_class import Base

class Product(Base):
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_name = Column(String, nullable= False)
    price = Column(Integer, nullable= False)
    quantity = Column(Integer, nullable= False)
    
