from pydantic import BaseModel, ConfigDict
from datetime import datetime
from app.models.task import Status, Priority

class TaskCreate(BaseModel):
    name: str
    description: str
    starts_at: datetime | None
    ends_at: datetime | None
    status: Status
    priority: Priority

class TaskResponse(BaseModel):
    id: int
    name: str
    description: str
    starts_at: datetime | None
    ends_at: datetime | None
    status: Status
    priority: Priority
    created_at: datetime | None
    project_id: int
    assignee_id: int | None

    model_config = ConfigDict(from_attributes=True)