from typing import List, Optional
from sqlalchemy import Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database.db import Base
from database.models.project import Project
from database.models.room import Room
from database.models.furniture import FurnitureType
from database.models.module import Module


class Product(Base):
    __tablename__ = "product"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    project_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("project.id", ondelete="CASCADE"),
        nullable=False
    )
    room_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("room.id"))
    type_id: Mapped[int] = mapped_column(
        ForeignKey("furniture_type.id"),
        nullable=False
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    width: Mapped[int] = mapped_column(Integer, nullable=False)  # в мм
    height: Mapped[int] = mapped_column(Integer, nullable=False)
    depth: Mapped[int] = mapped_column(Integer, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, default=1)
    placement_data: Mapped[Optional[dict]] = mapped_column(JSON)

    # Связи
    project: Mapped["Project"] = relationship(back_populates="products")
    room: Mapped[Optional["Room"]] = relationship(back_populates="products")
    type: Mapped["FurnitureType"] = relationship(back_populates="products")
    modules: Mapped[List["Module"]] = relationship(
        back_populates="product",
        cascade="all, delete-orphan"
    )