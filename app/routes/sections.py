from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

from app.models.section import Section
from app.schemas.section import SectionCreate
from app.dependencies.auth import get_current_user

# Router for section-related endpoints
router = APIRouter(
    prefix="/sections",
    tags=["sections"]
)

# Endpoint for creating a new section
@router.post("/{board_id}")
def create_section(board_id: int, data: SectionCreate, current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    section = Section(
        name=data.name,
        board_id=board_id,
        description=data.description
    )

    db.add(section)
    db.commit()
    db.refresh(section)

    return section