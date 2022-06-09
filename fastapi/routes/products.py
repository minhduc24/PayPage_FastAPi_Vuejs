from fastapi import Depends, APIRouter
from models.product import *
from sqlalchemy.orm import Session
from db.database import SessionLocal


router = APIRouter()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/product/{product_id}")
async def get_product1(product_id: int, db: Session = Depends(get_db)):
    product = get_product(db, product_id)
    return product

@router.post("/create_product")
async def create_product(product: ProductModel,db: Session = Depends(get_db)):
    product = create_new_product(db,product)
    return product
   

    