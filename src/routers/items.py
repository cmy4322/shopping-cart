from fastapi import APIRouter

router = APIRouter()

@router.get("/items/")

@router.get("/items/{item_id}")

@router.put("/items/{item_id}")

@router.post("/items/{item_id}")

@router.delete("/items/{item_id}")

