from fastapi import FastAPI

from app.database import Base, engine

from app.routes.auth import router as auth_router
from app.routes.boards import router as board_router
from app.routes.sections import router as section_router
from app.routes.tickets import router as ticket_router
from app.routes.invitations import router as invitation_router

from app.models.user import User
from app.models.board import Board
from app.models.section import Section
from app.models.ticket import Ticket
from app.models.invitation import Invitation

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Trello Clone API")

# Include routers for different endpoints
app.include_router(auth_router)
app.include_router(board_router)
app.include_router(section_router)
app.include_router(ticket_router)
app.include_router(invitation_router)


# Basic endpoint to check if the API is running
@app.get("/")
def home():
    return {"message": "Trello Clone API Running"}
