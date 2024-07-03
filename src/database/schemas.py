from pydantic import BaseModel

class CartBase(BaseModel):
    owner: str
    
class CartCreate(CartBase):
    pass

class Cart(CartBase):
    id: int

    class Config:
        orm_mode = True
