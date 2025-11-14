from pydantic import BaseModel, field_validator

class UserCreate(BaseModel):
    username: str
    password: str
    role: str 

    @field_validator("role")
    def validate_role(cls, v):
        allowed = ["admin", "user"]
        if v not in allowed:
            raise ValueError("Role must be either 'admin' or 'user'")
        return v

class UserResponse(BaseModel):
    # id: int
    username: str
    role: str

    class Config:
        from_attributes = True
