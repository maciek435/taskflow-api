from pydantic import BaseModel, ConfigDict
from datetime import datetime


class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime | None
    is_active: bool

    model_config = ConfigDict(from_attributes=True)