from pydantic import BaseModel

class NoteCreate(BaseModel):
    title: str
    content: str | None = None

class NoteResponse(BaseModel):
    # id: int
    title: str
    content: str | None
    owner_id: int
    created_by: int
    updated_by: int

    class Config:
        from_attributes = True