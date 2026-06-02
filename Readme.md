# Trello Clone API

A FastAPI-based backend for a Trello-like project management application. This API enables users to create and manage boards, organize work into sections, create tickets, and collaborate through team invitations.

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Database Models](#database-models)

## ✨ Features

- **User Authentication**: Register, login, and JWT-based token authorization
- **Board Management**: Create and manage project boards
- **Sections & Tickets**: Organize work with sections and individual tickets
- **Team Collaboration**: Invite team members to boards
- **Role-Based Access**: Users can only access their own boards
- **Secure Password Hashing**: Industry-standard password security

## 🛠 Tech Stack

- **Framework**: FastAPI
- **Database**: SQLAlchemy ORM
- **Authentication**: JWT (JSON Web Tokens)
- **Password Hashing**: bcrypt
- **Validation**: Pydantic
- **Server**: Uvicorn

## 📁 Project Structure

```
app/
├── main.py                 # FastAPI app initialization and router registration
├── config.py              # Environment configuration and settings
├── database.py            # SQLAlchemy engine, session, and base setup
├── dependencies/
│   └── auth.py            # Authentication dependencies (get_current_user)
├── models/                # SQLAlchemy ORM models
│   ├── user.py
│   ├── board.py
│   ├── section.py
│   ├── ticket.py
│   └── invitation.py
├── routes/                # FastAPI routers for endpoints
│   ├── auth.py            # Auth endpoints (register, login)
│   ├── boards.py          # Board endpoints
│   ├── sections.py        # Section endpoints
│   ├── tickets.py         # Ticket endpoints
│   └── invitations.py     # Invitation endpoints
├── services/              # Business logic layer
│   ├── auth_service.py    # User registration and login logic
│   ├── board_service.py   # Board operations
│   └── tickets_service.py # Ticket operations
├── schemas/               # Pydantic models for request/response validation
│   ├── auth.py
│   ├── user.py
│   ├── board.py
│   ├── section.py
│   └── ticket.py
└── utils/                 # Utility functions
    ├── jwt.py             # JWT token creation
    ├── security.py        # Password hashing and verification
    └── permissions.py     # Permission checks
```

## 🚀 Installation

### Prerequisites
- Python 3.8+
- pip or poetry
- MySQL server with a database and user configured

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sshah-03/Trello.git
   cd Trello
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables** (see Configuration section)

5. **Run the application**
   ```bash
   uvicorn app.main:app --reload
   ```

## ⚙️ Configuration

Create a `.env` file in the project root with the following variables:

```env
DATABASE_URL=mysql+pymysql://root:root123@localhost:3306/Trello
SECRET_KEY=your-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

**Environment Variables:**
- `DATABASE_URL`: Database connection string using MySQL and PyMySQL, for example `mysql+pymysql://user:password@host:3306/dbname`
- `SECRET_KEY`: Secret key for JWT encoding (use a strong, random string in production)
- `ALGORITHM`: JWT algorithm (HS256 recommended)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration time in minutes

## 🏃 Running the Application

### Development Mode (with auto-reload)
```bash
uvicorn app.main:app --reload
```

### Production Mode
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

**API Documentation:**
- Interactive Docs (Swagger UI): `http://localhost:8000/docs`
- Alternative Docs (ReDoc): `http://localhost:8000/redoc`

## 🧪 Testing

This project uses `pytest` for unit and integration testing. The test suite runs against an in-memory SQLite database by default and does not require an external database server.

### Install test dependencies
```bash
pip install -r requirements.txt
```

### Run all tests
```bash
pytest --cov=app tests/
```

### Coverage requirements
- At least 50% of project functions are covered by unit tests.
- At least 50% of API endpoints are covered by integration tests.

### Test layout
- `tests/conftest.py` — shared test fixtures and FastAPI client setup
- `tests/test_utils_security.py` — unit tests for password hashing and verification
- `tests/test_utils_jwt.py` — unit tests for JWT generation
- `tests/test_auth_service.py` — unit tests for user registration and login logic
- `tests/test_board_service.py` — board service unit tests
- `tests/test_api_endpoints.py` — integration tests for authentication, boards, and sections

## 📡 API Endpoints

## 📡 API Endpoints

### Authentication

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---|
| POST | `/auth/register` | Register a new user | ❌ |
| POST | `/auth/login` | Login and receive access token | ❌ |

### Boards

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---|
| POST | `/boards/` | Create a new board | ✅ |
| GET | `/boards/` | Get all boards owned by user | ✅ |

### Sections

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---|
| POST | `/sections/{board_id}` | Create a new section in a board | ✅ |

### Tickets

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---|
| POST | `/tickets/{section_id}` | Create a new ticket in a section | ✅ |

### Invitations

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---|
| POST | `/invitations/{board_id}` | Create an invitation for a board | ✅ |

## 🔐 Authentication

This API uses **JWT (JSON Web Tokens)** for authentication.

### Flow

1. **Register**: Send email, password, first_name, last_name to `/auth/register`
2. **Login**: Send email and password to `/auth/login` → receive `access_token`
3. **Authenticated Requests**: Include token in Authorization header:
   ```
   Authorization: Bearer <access_token>
   ```

### Example

```bash
# Register
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "securepassword",
    "first_name": "John",
    "last_name": "Doe"
  }'

# Login
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "securepassword"
  }'

# Response
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}

# Use token in subsequent requests
curl -X GET "http://localhost:8000/boards/" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

## 📊 Database Models

### User
```python
- id: Integer (Primary Key)
- email: String (Unique)
- hashed_password: String
- first_name: String
- last_name: String
- owned_boards: Relationship → Board
```

### Board
```python
- id: Integer (Primary Key)
- name: String
- description: String (Optional)
- owner_id: Integer (Foreign Key → User)
- owner: Relationship → User
- sections: Relationship → Section
```

### Section
```python
- id: Integer (Primary Key)
- name: String
- description: String (Optional)
- board_id: Integer (Foreign Key → Board)
- board: Relationship → Board
- tickets: Relationship → Ticket
```

### Ticket
```python
- id: Integer (Primary Key)
- title: String
- description: String (Optional)
- section_id: Integer (Foreign Key → Section)
- created_by: Integer (Foreign Key → User)
- assigned_to: Integer (Foreign Key → User, Optional)
- section: Relationship → Section
```

### Invitation
```python
- id: Integer (Primary Key)
- board_id: Integer (Foreign Key → Board)
- token: String (UUID)
```

## 🔄 Request/Response Flow

```
Client Request
    ↓
FastAPI Router (app/routes/*)
    ↓
Dependency Injection (get_db, get_current_user)
    ↓
Service Layer (app/services/*)
    ↓
SQLAlchemy Models (app/models/*)
    ↓
Database
    ↓
Response (JSON via Pydantic schemas)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 🆘 Support

For issues, questions, or suggestions, please open an issue on GitHub.
