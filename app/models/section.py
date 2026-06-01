from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

# This is a SQLAlchemy model for the Section table in the database. It inherits from the Base class, which is the declarative base for the SQLAlchemy models.
class Section(Base):
    __tablename__ = "sections"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)
    board_id = Column(Integer, ForeignKey("boards.id"))

    # This defines a relationship to the Board model. The back_populates argument specifies that the Board model will have a corresponding relationship back to the Section model.
    board = relationship("Board", back_populates="sections")

    # This defines a relationship to the Ticket model. The back_populates argument specifies that the Ticket model will have a corresponding relationship back to the Section model. The cascade option specifies that when a Section is deleted, all related Tickets will also be deleted.
    tickets = relationship(
        "Ticket",
        back_populates="section",
        cascade="all, delete")