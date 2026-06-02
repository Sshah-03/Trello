

def test_auth_register_and_login(client):
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


def test_create_and_list_boards(client):
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

    board_payload = {"name": "Integration Board", "description": "Board created from integration test"}
    create_response = client.post(
        "/boards/",
        headers={"Authorization": f"Bearer {token}"},
        json=board_payload,
    )
    assert create_response.status_code == 200
    board_json = create_response.json()
    assert board_json["name"] == "Integration Board"

    list_response = client.get(
        "/boards/",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert list_response.status_code == 200
    boards = list_response.json()
    assert isinstance(boards, list)
    assert len(boards) == 1
    assert boards[0]["name"] == "Integration Board"


def test_create_section_requires_auth(client):
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

    section_payload = {"name": "Backlog", "description": "Incoming tasks"}
    section_response = client.post(
        f"/sections/{board_id}",
        headers={"Authorization": f"Bearer {token}"},
        json=section_payload,
    )

    assert section_response.status_code == 200
    section_json = section_response.json()
    assert section_json["name"] == "Backlog"
    assert section_json["board_id"] == board_id
