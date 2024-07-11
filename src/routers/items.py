from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from src.database.database import get_session
from src.database import models, schemas, crud

router = APIRouter()

@router.post("/items/", response_model=schemas.Item, status_code=201)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_session)):
    db_item = crud.get_item_by_sku(db, sku=item.sku)
    if db_item:
        raise HTTPException(status_code=400, detail="SKU already exists")
    return crud.create_item(db=db, item=item)

@router.put("/items/{item_id}", response_model=schemas.Item, status_code=201)
def update_item_by_id(item_id: int, item:schemas.ItemUpdate, db: Session = Depends(get_session)):
    db_item = crud.update_item(db, item_id=item_id, item_update=item)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.get("/items/", response_model=list[schemas.Item], status_code=200)
def get_items(db: Session = Depends(get_session)):
    return crud.get_all_items(db)

# @router.get("/items/{item_id}")

@router.delete("/items/{item_id}", response_model=schemas.Item, status_code=200)
def delete_item(item_id: int, db: Session = Depends(get_session)):
    db_item = crud.delete_item(db, item_id=item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

