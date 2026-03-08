from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import JSONResponse

from core.api.dataset_router import dataset_router
from core.api.responces import CustomResponse
from core.database.database import create_tables
from core.database.seed import seed_all
from core.exceptions import CustomHTTPException
from core.log import get_logger, setup_logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logger()
    await create_tables()
    await seed_all()
    yield


logger = get_logger(__name__)
app = FastAPI(lifespan=lifespan)
router = APIRouter(prefix="/api")
router.include_router(dataset_router)


app.include_router(router)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"{request.url.path}: {exc}", exc_info=True)
    error_data = CustomResponse.from_exception(CustomHTTPException)
    return JSONResponse(
        status_code=500,
        content=error_data[500]["content"]["application/json"]["example"],
    )