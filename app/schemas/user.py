from pydantic import BaseModel, EmailStr

# User schema for registration and authentication
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str

# User schema for response (without password)
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str

    class Config:
        from_attributes = True