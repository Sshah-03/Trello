from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import settings

# This creates a SQLAlchemy engine using the database URL from the settings.
engine = create_engine(settings.DATABASE_URL)

# This creates a sessionmaker, which is a factory for creating new SQLAlchemy sessions. The autocommit and autoflush options are set to False, which means that changes to the database will not be automatically committed or flushed.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False, 
    bind=engine)

# This creates a base class for the SQLAlchemy models. The declarative_base function returns a new base class that can be used to define the models.
Base = declarative_base()

# This function is a dependency that can be used in the FastAPI routes to get a database session. It creates a new session, yields it, and then closes it after the request is done.
def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()