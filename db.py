import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base
from fastapi import Depends
from typing import Generator

DB_URL = os.getenv("DATABASE_URL", "sqlite:///./test_assets.db")
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Ensure tables are created on first run (OK for test/demo)
Base.metadata.create_all(bind=engine)

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
