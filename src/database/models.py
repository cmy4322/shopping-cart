from sqlmodel import Field, SQLModel

class Cart(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    owner: str

# class Item(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     name: str
#     price: int # Price Type?

# class ItemsInCart(SQLModel, table=True):
#     cart_id: int = Field(foreign_key="cart.id")
#     item_id: int = Field(foreign_key="item.id")
#     quantity: int 
