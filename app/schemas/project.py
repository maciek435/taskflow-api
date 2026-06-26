from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ProjectCreate(BaseModel):
    name: str
    description: str
    
class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime | None
    owner_id: int

    model_config = ConfigDict(from_attributes=True)