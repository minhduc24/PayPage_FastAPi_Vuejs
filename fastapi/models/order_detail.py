from datetime import datetime
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.entities.order_detail import OrderDetail

class OrderDetailModel(BaseModel):
    order_id: int   
    product_id: int 
    pay_method: str
    created_at: datetime
    
