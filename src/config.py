from functools import lru_cache
import logging
from pydantic import AnyUrl
from pydantic_settings import BaseSettings

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Settings(BaseSettings):
    database_url: AnyUrl = None

@lru_cache()
def get_settings() -> BaseSettings:
    logger.info("Loading config from environment...")
    return Settings()