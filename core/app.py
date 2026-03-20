from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI

from core.api.dataset_router import dataset_router
from core.exceptions.exception_handlers import register_exception_handlers
from core.log import get_logger, setup_logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logger()
    yield


logger = get_logger(__name__)
app = FastAPI(lifespan=lifespan)
router = APIRouter(prefix="/api")
router.include_router(dataset_router)


app.include_router(router=router)

register_exception_handlers(app=app)
