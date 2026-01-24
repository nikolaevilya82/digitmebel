from typing import Optional, List
import uuid
from sqlalchemy import String, Text, Enum, ForeignKey, Integer, Float, JSON, DateTime, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.db import Base
from database.models.project import Project
from database.models.product import Product


class Room(Base):
    __table_name__ = "room"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    project_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("project.id", ondelete="CASCADE"),
        nullable=False
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    width: Mapped[int] = mapped_column(Integer, nullable=False)  # в мм
    height: Mapped[int] = mapped_column(Integer, nullable=False)
    depth: Mapped[int] = mapped_column(Integer, nullable=False)
    layout_data: Mapped[Optional[dict]] = mapped_column(JSON)

    # Связи
    project: Mapped["Project"] = relationship(back_populates="rooms")
    products: Mapped[List["Product"]] = relationship(back_populates="room")
