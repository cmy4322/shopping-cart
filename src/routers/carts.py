from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from src.database.database import get_session
from src.database import models, schemas, crud

router = APIRouter()

@router.post("/carts/", response_model=schemas.Cart, status_code=201)
def create_cart(cart: schemas.CartCreate, db: Session = Depends(get_session)):
    db_cart = crud.get_cart_by_owner(db, owner=cart.owner)
    if db_cart:
        raise HTTPException(status_code=400, detail="Owner already has a cart")
    return crud.create_cart(db=db, cart=cart)

# @router.get("/carts/{cart_id}", response_model=schemas.Cart, status_code=200)
# def get_cart_by_id(cart_id: int, db: Session = Depends(get_session)):
#     db_cart = crud.get_carts()

@router.delete("/carts/{cart_id}", response_model=schemas.Cart, status_code=200)
def delete_cart(cart_id: int, db: Session = Depends(get_session)):
    db_cart = crud.delete_cart(db, cart_id=cart_id)
    if not db_cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    return db_cart

@router.post("/carts/{cart_id}/items/{item_id}", response_model=schemas.ItemsInCartBase, status_code=201)
def update_cart(cart_id: int, item_id: int, quantity: int, db: Session = Depends(get_session)):
    return crud.add_item_to_cart(db, cart_id=cart_id, item_id=item_id, quantity=quantity)

@router.get("/carts/{cart_id}", response_model=list[schemas.ItemsInCartBase], status_code=200)
def get_cart_items(cart_id: int, db: Session = Depends(get_session)):
    return crud.get_cart_items(db, cart_id=cart_id)