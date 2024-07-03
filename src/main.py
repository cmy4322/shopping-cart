from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging

from src.database.database import create_database_and_tables
from src.routers import carts

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting app...")
    create_database_and_tables()
    yield
    logger.info("Shutting down app...")
    logger.info("Shut down app.")

def get_app() -> FastAPI:
    app = FastAPI(title="FastAPI Shopping Cart Application", lifespan=lifespan)
    app.include_router(carts.router)
    return app

app = get_app()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}