from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

# This is a SQLAlchemy model for the Board table in the database. It inherits from the Base class, which is the declarative base for the SQLAlchemy models.
class Board(Base):
    __tablename__ = "boards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    

    # This defines a relationship to the User model. The back_populates argument specifies that the User model will have a corresponding relationship back to the Board model.
    owner = relationship("User", back_populates="owned_boards")

    sections = relationship(
        "Section",
        back_populates="board",
        cascade="all, delete")