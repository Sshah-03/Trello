from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate
from app.dependencies.auth import get_current_user

# Router for ticket-related endpoints
router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)

# Endpoint for creating a new ticket within a section
@router.post("/{section_id}")
def create_ticket(section_id: int, data: TicketCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):

    ticket = Ticket(
        section_id=section_id,
        title=data.title,
        description=data.description,
        assigned_to=data.assigned_to,
        created_by=current_user.id
    )

    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    return ticket