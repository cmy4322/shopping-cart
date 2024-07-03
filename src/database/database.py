import logging
from sqlmodel import Session, SQLModel, create_engine
from src.config import get_settings

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

DB_SETTINGS = get_settings()
DB_URL = str(DB_SETTINGS.database_url)

engine = create_engine(DB_URL)

def create_database_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    logger.info("Initialising db session...")
    with Session(engine) as session:
        yield session