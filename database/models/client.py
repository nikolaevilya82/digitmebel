from datetime import datetime, timezone
from typing import List, Optional
from sqlalchemy import String, DateTime, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database.db import Base
from database.models.project import Project


class Client(Base):
    __tablename__ = "client"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    registration_date: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc)
    )
    notes: Mapped[Optional[str]] = mapped_column(Text)

    # Связи
    projects: Mapped[List["Project"]] = relationship(
        back_populates="client",
        cascade="all, delete-orphan"
    )