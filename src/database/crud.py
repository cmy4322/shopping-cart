from sqlmodel import Session, select

from src.database import models, schemas

def create_cart(db: Session, cart: schemas.CartCreate):
    db_cart = models.Cart(owner=cart.owner)
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return db_cart

def get_cart_by_owner(db: Session, owner: str):
    return db.exec(select(models.Cart).where(models.Cart.owner == owner)).first()

# def get_carts(db: Session, zero: int=0):
#     return db.query(models.Cart).offset(zero).all()

def delete_cart(db: Session, cart_id: int):
    db_cart = db.exec(select(models.Cart).where(models.Cart.id == cart_id)).first()
    if not db_cart:
        return None
    db.delete(db_cart)
    db.commit()
    return db_cart

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(
        name = item.name,
        description = item.description,
        sku = item.sku,
        category = item.category,
        price = item.price,
        brand = item.brand
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_item_by_sku(db: Session, sku: str):
    return db.exec(select(models.Item).where(models.Item.sku == sku)).first()

def update_item(db: Session, item_id: int, item_update: schemas.ItemUpdate):
    item_data = item_update.model_dump(exclude_unset=True)

    db_item = db.exec(select(models.Item).where(models.Item.id == item_id)).first()
    if not db_item:
        return db_item
    for key, value in item_data.items():
        setattr(db_item, key, value)

    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_all_items(db: Session):
    return db.exec(select(models.Item)).all()

def delete_item(db: Session, item_id: int):
    db_item = db.exec(select(models.Item).where(models.Item.id == item_id)).first()
    if not db_item:
        return None
    db.delete(db_item)
    db.commit()
    return db_item

def add_item_to_cart(db: Session, cart_id: int, item_id: int, quantity: int):
    db_cart_item = db.exec(select(models.ItemsInCart).where(
        models.ItemsInCart.cart_id == cart_id and
        models.ItemsInCart.item_id == item_id)).first()
    if db_cart_item:
        setattr(db_cart_item, "quantity", db_cart_item.quantity + quantity)
    else:
        db_cart_item = models.ItemsInCart(cart_id=cart_id, item_id=item_id, quantity=quantity)
    db.add(db_cart_item)
    db.commit()
    db.refresh(db_cart_item)
    return db_cart_item

def get_cart_items(db: Session, cart_id: int):
    return db.exec(select(models.ItemsInCart).where(models.ItemsInCart.cart_id == cart_id)).all()