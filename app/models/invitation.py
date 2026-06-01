from sqlalchemy import Column, Integer, String, ForeignKey

from app.database import Base

# This is a SQLAlchemy model for the Invitation table in the database. It inherits from the Base class, which is the declarative base for the SQLAlchemy models.
class Invitation(Base):
    __tablename__ = "invitations"

    id = Column(Integer, primary_key=True, index=True)
    board_id = Column(Integer, ForeignKey("boards.id"))
    token = Column(String(255), unique=True)   
