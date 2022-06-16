from datetime import datetime
from sqlalchemy.orm import  Session
from db.entities.order import Order
from db.entities.user import User
from db.entities.order_detail import OrderDetail
from models.user import *

def create_order(db: Session, order):
    orderInstance = Order(
        user_id = order.user_id,
        created_at = datetime.now()
    )
    db.add(orderInstance)
    db.commit()
    order_details = []
    total = 0
    for order_detail in order.order_details:
        order_details.append(
            OrderDetail(
                order_id = orderInstance.id,
                product_id = order_detail.product_id,     
                pay_method = order_detail.pay_method,
                total_price = order_detail.total_price,
                created_at = datetime.now()
            )
        )
    total = order_detail.total_price
    db.bulk_save_objects(order_details)
    db.commit()
    user1 = db.query(User).filter(User.id == orderInstance.user_id)
    user1.update({'accumulate_points': total})
    db.bulk_save_objects(user1)
    db.commit()
    print(orderInstance.user_id)
    return {"ok": True}
