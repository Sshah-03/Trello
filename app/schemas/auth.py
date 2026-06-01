from pydantic import BaseModel

# Schema for user login
class LoginSchema(BaseModel):
    email: str
    password: str

# Schema for token response
class TokenResponse(BaseModel):
    access_token: str
    token_type: str
