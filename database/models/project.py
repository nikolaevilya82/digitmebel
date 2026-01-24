from datetime import datetime, timezone
from typing import List, Optional
import uuid
from sqlalchemy import String, Text, Enum, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database.db import Base
from database.models.client import Client
from database.models.room import Room
from database.models.product import Product
from database.models.calculation import Calculation


class Project(Base):
    __table_name__ =  "project"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    client_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("client.id", ondelete="CASCADE"),
        nullable=False
    )
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    status: Mapped[str] = mapped_column(
        Enum("черновик", "расчет", "утвержден", "в производстве", "готов", "отменен",
             name="project_status"),
        default="черновик"
    )
    description: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc)
    )

    # связи
    client: Mapped["Client"] = relationship(back_populates="projects")
    rooms: Mapped[List["Room"]] = relationship(
        back_populates="project",
        cascade="all, delete-orphan"
    )
    products: Mapped[List["Product"]] = relationship(
        back_populates="project",
        cascade="all, delete-orphan"
    )
    calculations: Mapped[List["Calculation"]] = relationship(
        back_populates="project",
        cascade="all, delete-orphan"
    )
