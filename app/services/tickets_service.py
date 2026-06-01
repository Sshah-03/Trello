from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.ticket import Ticket
from app.models.section import Section
from app.schemas import section

# Service for creating a new ticket in a section
def movie_ticket(ticket:Ticket, new_Section_id:int, db: Session):
    old_section = db.query(Section).filter(Section.id == ticket.section_id).first()
    
    new_Section_id = db.query(Section).filter(Section.id == new_Section_id).first()

    if old_section.board_id != new_Section_id.board_id:
        raise HTTPException(status_code=400, detail="Sections must belong to the same board")

    ticket.section_id = new_Section_id.id
    db.commit()
    db.refresh(ticket)
    
    return ticket