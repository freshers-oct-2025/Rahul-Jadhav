from pydantic import BaseModel
from typing import Any

class Response(BaseModel):
    message: str
    data: Any | None = None

    class Config:
        from_attributes = True
