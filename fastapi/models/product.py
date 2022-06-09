from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.entities.product import Product


class ProductModel(BaseModel):
    id: int 
    product_name: str
    price: int
    quantity: int
    
    
    
def get_product(db: Session, product_id: int):
    result = db.query(Product).filter(Product.id == product_id).first()
    return result
    

def create_new_product(db: Session, product: ProductModel):
    product = Product(
        id = product.id,
        product_name = product.product_name, 
        price = product.price, 
        quantity = product.quantity
    )
    result = db.add(product)
    db.commit()
    db.refresh(product)
    return result