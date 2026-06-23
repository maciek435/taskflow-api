from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.database import Base
from sqlalchemy import ForeignKey

class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    owner: Mapped["User"] = relationship(back_populates="projects")
    tasks: Mapped[list["Task"]] = relationship(back_populates="project")