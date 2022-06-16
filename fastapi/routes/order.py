from fastapi import APIRouter, Depends
from requests import Session
from models.order import * 
from db.database import SessionLocal
from pydantic import BaseModel
from typing import List
from routes.users import UserUpdate

router = APIRouter()

class OrderDetailss(BaseModel):
    product_id: int 
    pay_method: str
    total_price: int

class Order(BaseModel):
    user_id: int
    order_details: List[OrderDetailss]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

@router.post("/orders")
async def create_order1(order: Order, db: Session = Depends(get_db) ):
    order = create_order(db, order)
    return order