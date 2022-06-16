from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.entities.product import Product


class ProductModel(BaseModel):
    product_name: str
    price: int
    quantity: int
    
    
    
def get_product(db: Session, product_id: int):
    result = db.query(Product).filter(Product.id == product_id).first()
    return result
    

def create_new_product(db: Session, product: ProductModel):
    product = Product(
        product_name = product.product_name, 
        price = product.price, 
        quantity = product.quantity
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return {"ok": True}


def delete_product(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    db.delete(product)
    db.commit()
    return {"ok": True}