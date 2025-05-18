from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import AsyncGenerator, Generator

# Ganti URL sesuai konfigurasi Anda
DATABASE_URL = "postgresql+asyncpg://user:password@localhost/rt_siaga"

# Async Engine & Session
async_engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False
)

# Sync Engine & Session (jika masih butuh sync)
sync_engine = create_engine(DATABASE_URL.replace("asyncpg", "psycopg2"))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

Base = declarative_base()

# Dependency Injection untuk Async
async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session

# Dependency Injection untuk Sync
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()