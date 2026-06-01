import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

from app.models.invitation import Invitation
from app.dependencies.auth import get_current_user

# Router for invitation-related endpoints
router = APIRouter(
    prefix="/invitations",
    tags=["Invitations"]
)

# Endpoint for creating a new invitation for a board
@router.post("/{board_id}")
def create_invitation(board_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):

    invitation = Invitation(
        board_id=board_id,
        token=str(uuid.uuid4())
    )

    db.add(invitation)
    db.commit()
    db.refresh(invitation)

    return invitation