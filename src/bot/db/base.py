from contextlib import asynccontextmanager

from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import declarative_base

from bot.config import config

postgres_url = (
    f"postgresql+asyncpg://"
    f"{config.POSTGRES_USER}:"
    f"{config.POSTGRES_PASSWORD}@"
    f"{config.POSTGRES_HOST}:"
    f"{config.POSTGRES_PORT}/"
    f"{config.POSTGRES_DB}"
)
engine = create_async_engine(
    postgres_url,
    echo=True,
)
Base: DeclarativeMeta = declarative_base()
Session = async_sessionmaker(bind=engine, autocommit=False, autoflush=False, expire_on_commit=False)


@asynccontextmanager
async def session(**kwargs):
    new_session: AsyncSession = Session(**kwargs)
    try:
        yield new_session
    except Exception as e:
        await new_session.rollback()
        logger.error(f"Error in session: {e}")
        raise
    finally:
        await new_session.close()
