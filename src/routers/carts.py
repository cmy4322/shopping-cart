from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from src.database.database import get_session
from src.database import models, schemas, crud

router = APIRouter()

@router.post("/carts/", response_model=schemas.Cart, status_code=201)
def create_cart(cart: schemas.CartCreate, db: Session = Depends(get_session)):
    new_cart = crud.get_cart_by_owner(db, owner=cart.owner)
    if new_cart:
        raise HTTPException(status_code=400, detail="Owner already has a cart")
    return crud.create_cart(db=db, cart=cart)

# @router.get("/carts/{cart_id}")

# @router.delete("/carts/{cart_id}")

# @router.post("/carts/{cart_id}/items/")
