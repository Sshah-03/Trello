from pydantic import BaseModel

# Schema for ticket creation
class TicketCreate(BaseModel):
    title: str
    description: str
    assigned_to: int  | None = None  # User ID of the assignee

# Schema for ticket update
class TicketUpdate(BaseModel):
    title: str
    description: str
    assigned_to: int | None = None  # User ID of the assignee
    section_id: int  # ID of the section the ticket belongs to