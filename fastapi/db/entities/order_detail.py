from sqlalchemy import Column, DateTime, Integer, String
from db.base_class import Base

class Order_detail(Base):

    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, nullable= False)
    product_id = Column(Integer, nullable= False)
    pay_method = Column(String, nullable= False)
    created_at = Column(DateTime, nullable= False)
    
