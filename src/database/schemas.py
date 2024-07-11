from decimal import Decimal
from pydantic import BaseModel

class CartBase(BaseModel):
    owner: str

class CartCreate(CartBase):
    pass

class Cart(CartBase):
    id: int

    class Config:
        orm_mode = True

class ItemBase(BaseModel):
    name: str
    description: str
    sku: str
    category: str
    price: Decimal
    brand: str

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

class ItemUpdate(ItemBase):
    name: str | None = None
    description: str | None = None
    sku: str | None = None
    category: str | None = None
    price: Decimal | None = None
    brand: str | None = None 

class ItemsInCartBase(BaseModel):
    cart_id: int
    item_id: int
    quantity: int
    
    class Config:
        orm_mode = True


class HealthCheck(BaseModel):
    status: str = "ok"