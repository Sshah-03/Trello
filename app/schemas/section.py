from pydantic import BaseModel

# Schema for Section creation
class SectionCreate(BaseModel):
    name: str
    description: str

# Schema for Section update
class SectionUpdate(BaseModel):
    name: str
    description: str
