from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from src.database.database import get_session
from src.database import models, schemas, crud

router = APIRouter()
@router.get("/health", response_model=schemas.HealthCheck, status_code=status.HTTP_200_OK)
def get_health():
    return schemas.HealthCheck(status="ok")