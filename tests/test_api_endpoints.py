import pytest


class TestAuthenticationEndpoints:
    """Test suite for authentication-related API endpoints."""

    def test_auth_register_and_login(self, client):
        """Test user registration and subsequent login."""
        register_payload = {
            "email": "intuser@example.com",
            "password": "IntTest123$",
            "first_name": "Integration",
            "last_name": "Tester"
        }

        register_response = client.post("/auth/register", json=register_payload)
        assert register_response.status_code == 200
        assert register_response.json()["email"] == "intuser@example.com"

        login_payload = {
            "email": "intuser@example.com",
            "password": "IntTest123$"
        }
        login_response = client.post("/auth/login", json=login_payload)
        assert login_response.status_code == 200
        token_data = login_response.json()
        assert token_data["token_type"] == "bearer"
        assert "access_token" in token_data


class TestBoardEndpoints:
    """Test suite for board-related API endpoints."""

    @pytest.fixture
    def authenticated_client(self, client):
        """Fixture to provide an authenticated client with token."""
        register_payload = {
            "email": "boardint@example.com",
            "password": "BoardPass123$",
            "first_name": "Board",
            "last_name": "Integration"
        }
        client.post("/auth/register", json=register_payload)
        login_response = client.post("/auth/login", json={
            "email": "boardint@example.com",
            "password": "BoardPass123$"
        })
        token = login_response.json()["access_token"]
        
        class AuthenticatedClient:
            def __init__(self, client, token):
                self._client = client
                self.token = token
            
            def post(self, url, **kwargs):
                headers = kwargs.pop("headers", {})
                headers["Authorization"] = f"Bearer {self.token}"
                return self._client.post(url, headers=headers, **kwargs)
            
            def get(self, url, **kwargs):
                headers = kwargs.pop("headers", {})
                headers["Authorization"] = f"Bearer {self.token}"
                return self._client.get(url, headers=headers, **kwargs)
        
        return AuthenticatedClient(client, token)

    def test_create_and_list_boards(self, authenticated_client):
        """Test board creation and retrieval."""
        board_payload = {"name": "Integration Board", "description": "Board created from integration test"}
        create_response = authenticated_client.post(
            "/boards/",
            json=board_payload,
        )
        assert create_response.status_code == 200
        board_json = create_response.json()
        assert board_json["name"] == "Integration Board"

        list_response = authenticated_client.get("/boards/")
        assert list_response.status_code == 200
        boards = list_response.json()
        assert isinstance(boards, list)
        assert len(boards) == 1
        assert boards[0]["name"] == "Integration Board"


class TestSectionEndpoints:
    """Test suite for section-related API endpoints."""

    @pytest.fixture
    def authenticated_client_with_board(self, client):
        """Fixture to provide an authenticated client with a board."""
        register_payload = {
            "email": "sectionint@example.com",
            "password": "SectionPass123$",
            "first_name": "Section",
            "last_name": "Integration"
        }
        client.post("/auth/register", json=register_payload)
        login_response = client.post("/auth/login", json={
            "email": "sectionint@example.com",
            "password": "SectionPass123$"
        })
        token = login_response.json()["access_token"]

        board_payload = {"name": "Section Board", "description": "Board for section tests"}
        create_board_response = client.post(
            "/boards/",
            headers={"Authorization": f"Bearer {token}"},
            json=board_payload,
        )
        board_id = create_board_response.json()["id"]
        
        class AuthenticatedClientWithBoard:
            def __init__(self, client, token, board_id):
                self._client = client
                self.token = token
                self.board_id = board_id
            
            def post(self, url, **kwargs):
                headers = kwargs.pop("headers", {})
                headers["Authorization"] = f"Bearer {self.token}"
                return self._client.post(url, headers=headers, **kwargs)
        
        return AuthenticatedClientWithBoard(client, token, board_id)

    def test_create_section_requires_auth(self, authenticated_client_with_board):
        """Test section creation with authentication."""
        section_payload = {"name": "Backlog", "description": "Incoming tasks"}
        section_response = authenticated_client_with_board.post(
            f"/sections/{authenticated_client_with_board.board_id}",
            json=section_payload,
        )

        assert section_response.status_code == 200
        section_json = section_response.json()
        assert section_json["name"] == "Backlog"
        assert section_json["board_id"] == authenticated_client_with_board.board_id
