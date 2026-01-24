from datetime import datetime, timezone
from decimal import Decimal
from typing import List, Optional
import uuid
from sqlalchemy import String, Enum, ForeignKey, Integer, Float, DateTime, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database.db import Base
from database.models.project import Project


class Calculation(Base):
    __tablename__ = "calculation"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    project_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("project.id", ondelete="CASCADE"),
        nullable=False
    )
    version: Mapped[int] = mapped_column(Integer, nullable=False)
    total_material_cost: Mapped[Decimal] = mapped_column(Numeric(12, 2), default=0)
    total_hardware_cost: Mapped[Decimal] = mapped_column(Numeric(12, 2), default=0)
    workmanship_cost: Mapped[Decimal] = mapped_column(Numeric(12, 2), default=0)
    margin_percent: Mapped[float] = mapped_column(Float, default=0.0)
    total_price: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    created_by: Mapped[Optional[str]] = mapped_column(String(100))

    # Составной уникальный ключ
    __table_args__ = (('unique_project_version', 'project_id', 'version'),)

    # Связи
    project: Mapped["Project"] = relationship(back_populates="calculations")
    details: Mapped[List["CalculationDetail"]] = relationship(
        back_populates="calculation",
        cascade="all, delete-orphan"
    )


class CalculationDetail(Base):
    __tablename__ = "calculation_detail"

    id: Mapped[int] = mapped_column(primary_key=True)
    calculation_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("calculation.id", ondelete="CASCADE"),
        nullable=False
    )
    item_type: Mapped[str] = mapped_column(
        Enum("material", "hardware", "work", "other", name="cost_item_type"),
        nullable=False
    )
    item_id: Mapped[Optional[uuid.UUID]]  # может быть NULL для работ
    item_name: Mapped[str] = mapped_column(String(200), nullable=False)
    quantity: Mapped[float] = mapped_column(Float, nullable=False)
    unit_price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    total: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)

    # Связи
    calculation: Mapped["Calculation"] = relationship(back_populates="details")

# TODO вынести все расчеты деталей в отдельную логику
