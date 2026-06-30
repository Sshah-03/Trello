import pytest
from app.models.board import Board
from app.models.user import User
from app.schemas.board import BoardCreate
from app.services.board_service import BoardService


class TestBoardService:
    """Test suite for board service functionality."""

    @pytest.fixture
    def board_owner(self, db_session):
        """Fixture to create a board owner user."""
        user = User(
            email="boardowner@example.com",
            hashed_password="hashed",
            first_name="Board",
            last_name="Owner"
        )
        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)
        return user

    @pytest.fixture
    def board_service(self, db_session):
        """Fixture to provide a BoardService instance."""
        return BoardService(db_session)

    def test_create_board_assigns_owner(self, db_session, board_service, board_owner):
        """Test that creating a board correctly assigns the owner."""
        board_data = BoardCreate(name="Sprint Planning", description="Board for sprint planning")

        board = board_service.create_board(board_data, board_owner)

        assert board.id is not None
        assert board.owner_id == board_owner.id
        assert board.name == "Sprint Planning"

    def test_get_all_boards_returns_only_user_boards(self, db_session, board_service):
        """Test that get_all_boards returns only boards owned by the specified user."""
        owner = User(
            email="owner@example.com",
            hashed_password="hashed",
            first_name="Owner",
            last_name="User"
        )
        other_user = User(
            email="other@example.com",
            hashed_password="hashed",
            first_name="Other",
            last_name="User"
        )
        db_session.add_all([owner, other_user])
        db_session.commit()
        db_session.refresh(owner)
        db_session.refresh(other_user)

        board_service.create_board(BoardCreate(name="Owner Board", description="Owner only"), owner)
        board_service.create_board(BoardCreate(name="Other Board", description="Other user"), other_user)

        boards = board_service.get_all_boards(owner)

        assert len(boards) == 1
        assert boards[0].owner_id == owner.id
