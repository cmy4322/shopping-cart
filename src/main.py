from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging
from prometheus_fastapi_instrumentator import Instrumentator, metrics

from src.database.database import create_database_and_tables
from src.routers import carts, items, healthcheck

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
    app.include_router(items.router)
    app.include_router(healthcheck.router)
    return app

app = get_app()

# Instrumentator().instrument(app).expose(app)
instrumentator = Instrumentator(
    should_group_status_codes=False,
    should_ignore_untemplated=True,
    should_respect_env_var=True,
    should_instrument_requests_inprogress=True,
    excluded_handlers=[".*admin.*", "/metrics"],
    env_var_name="ENABLE_METRICS",
    inprogress_name="inprogress",
    inprogress_labels=True,
)

instrumentator.instrument(app).expose(app)
