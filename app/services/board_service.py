from sqlalchemy.orm import Session

from app.models.board import Board

from app.schemas.board import BoardCreate


class BoardService:

    def __init__(self, db: Session):
        self.db = db

    def create_board(
        self,
        data: BoardCreate,
        current_user
    ):

        board = Board(
            name=data.name,
            description=data.description,
            owner_id=current_user.id
        )

        self.db.add(board)

        self.db.commit()

        self.db.refresh(board)

        return board

    def get_all_boards(
        self,
        current_user
    ):

        return self.db.query(Board).filter(
            Board.owner_id == current_user.id
        ).all()