from pydantic import BaseModel

#Schema for creating a new board
class BoardCreate(BaseModel):
    name: str
    description: str

#Schema for updating an existing board
class BoardUpdate(BaseModel):
    name: str
    description: str