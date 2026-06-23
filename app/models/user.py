from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    is_active: Mapped[bool] = mapped_column(default=True)
    projects: Mapped[list["Project"]] = relationship(back_populates="owner")
    tasks: Mapped[list["Task"]] = relationship(back_populates="owner")