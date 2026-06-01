from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

# This is a SQLAlchemy model for the User table in the database. It inherits from the Base class, which is the declarative base for the SQLAlchemy models.
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    
    # This defines a relationship to the Board model. The back_populates argument specifies that the Board model will have a corresponding relationship back to the User model.
    owned_boards = relationship("Board", back_populates="owner")