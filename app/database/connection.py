
from sqlalchemy import create_engine, text

from app.core.config import settings


def get_engine():

    if not settings.DATABASE_URL:
        raise ValueError("DATABASE_URL is missing")

    # pool_pre_ping checks connections before using them
    engine = create_engine(
        settings.DATABASE_URL,
        pool_pre_ping=True
    )

    return engine


def test_connection():

    engine = get_engine()

    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT 1")
        )

        return result.scalar_one() == 1
