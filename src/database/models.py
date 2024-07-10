from decimal import Decimal
from sqlalchemy import Column, TEXT
from sqlmodel import Field, SQLModel

class Cart(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    owner: str = Field(index=True)

class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str = Field(sa_column=Column(TEXT))
    sku: str = Field(unique=True)
    category: str
    price: Decimal = Field(default=0, decimal_places=2)
    brand: str

class ItemsInCart(SQLModel, table=True):
    cart_id: int = Field(foreign_key="cart.id", primary_key=True)
    item_id: int = Field(foreign_key="item.id", primary_key=True)
    quantity: int