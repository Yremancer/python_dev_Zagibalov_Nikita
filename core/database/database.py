from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.ext.declarative import declarative_base

from core.log import logger

MAIN_DATABASE_URL = "sqlite+aiosqlite:///core/database/main.db"
LOGS_DATABASE_URL = "sqlite+aiosqlite:///core/database/logs.db"


Base = declarative_base()
BaseLog = declarative_base()

main_engine = create_async_engine(MAIN_DATABASE_URL)
main_async_session_maker = async_sessionmaker(
    main_engine, expire_on_commit=False
)

logs_engine = create_async_engine(LOGS_DATABASE_URL)
logs_async_session_maker = async_sessionmaker(
    logs_engine, expire_on_commit=False
)


async def get_main_db_session_obj() -> AsyncGenerator[AsyncSession, None]:
    session = main_async_session_maker()
    async with session.begin():
        yield session
    await session.close()


async def get_logs_db_session_obj() -> AsyncGenerator[AsyncSession, None]:
    session = logs_async_session_maker()
    async with session.begin():
        yield session
    await session.close()


async def create_tables():
    import core.database.models.logs  # noqa: F401
    import core.database.models.main  # noqa: F401

    async with main_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with logs_engine.begin() as conn:
        await conn.run_sync(BaseLog.metadata.create_all)
    logger.info("Tables created")
