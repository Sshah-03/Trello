from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.board import BoardCreate

from app.services.board_service import BoardService

from app.dependencies.auth import get_current_user


router = APIRouter(
    prefix="/boards",
    tags=["Boards"]
)


@router.post("/")
def create_board(
    data: BoardCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    board_service = BoardService(db)

    return board_service.create_board(
        data,
        current_user
    )


@router.get("/")
def get_boards(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    board_service = BoardService(db)

    return board_service.get_all_boards(
        current_user
    )