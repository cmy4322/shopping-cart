from sqlmodel import Session, select

from src.database import models, schemas

def create_cart(db: Session, cart: schemas.CartCreate):
    db_cart = models.Cart(owner=cart.owner)
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return db_cart

def get_cart_by_owner(db: Session, owner: str):
    return db.query(models.Cart).filter(models.Cart.owner == owner).first()

def get_carts(db: Session, zero: int=0):
    return db.query(models.Cart).offset(zero).all()