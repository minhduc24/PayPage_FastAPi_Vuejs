from sqlalchemy import Column, DateTime, Integer, String
from db.base_class import Base

class OrderDetail(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)
    pay_method = Column(String, nullable=False)
    total_price = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable= False)
    
