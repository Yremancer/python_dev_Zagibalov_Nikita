from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends

from core.database.database import create_tables, get_main_db_session_obj
from core.database.models.main import UserOrm

@asynccontextmanager
async def lifespawn(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=lifespawn)


@app.get("/")
async def root(main_session=Depends(get_main_db_session_obj)):
    main_session.add(UserOrm(login="test", email="test@example.com"))
    await main_session.commit()
    return {"message": "User created"}