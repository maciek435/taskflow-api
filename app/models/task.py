from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.database import Base
from sqlalchemy import ForeignKey
from enum import Enum

class Status(Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"

class Priority(Enum):
    HIGH = "high"
    MID = "mid"
    LOW = "low"

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    starts_at: Mapped[datetime | None] = mapped_column(default=None)
    ends_at: Mapped[datetime | None] = mapped_column(default=None)
    status: Mapped[Status] = mapped_column(default=Status.TODO)
    priority: Mapped[Priority]  = mapped_column(default=Priority.HIGH)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))
    assignee_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"), default=None)
    project: Mapped["Project"] = relationship(back_populates="tasks")
    owner: Mapped["User"] = relationship(back_populates="tasks")