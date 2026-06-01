from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base   

# This is a SQLAlchemy model for the Ticket table in the database. It inherits from the Base class, which is the declarative base for the SQLAlchemy models.
class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)
    section_id = Column(Integer, ForeignKey("sections.id"))
    created_by = Column(Integer, ForeignKey("users.id"))
    assigned_to = Column(Integer, ForeignKey("users.id"), nullable=True)

    # This defines a relationship to the Section model. The back_populates argument specifies that the Section model will have a corresponding relationship back to the Ticket model.
    section = relationship("Section", back_populates="tickets")