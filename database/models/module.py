from typing import List, Optional
from sqlalchemy import Integer, String, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database.db import Base
from database.models.product import Product


class Module(Base):
    __tablename__ = "module"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    product_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("product.id", ondelete="CASCADE"),
        nullable=False
    )
    parent_module_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("module.id"))
    module_type: Mapped[str] = mapped_column(
        Enum("корпус", "фасад", "полка", "ящик", "дверца", "столешница", "прочее",
             name="module_type"),
        nullable=False
    )
    name: Mapped[Optional[str]] = mapped_column(String(100))
    width: Mapped[int] = mapped_column(Integer, nullable=False)
    height: Mapped[int] = mapped_column(Integer, nullable=False)
    depth: Mapped[int] = mapped_column(Integer, nullable=False)
    assembly_instructions: Mapped[Optional[str]] = mapped_column(Text)

    # Связи
    product: Mapped["Product"] = relationship(back_populates="modules")
    parent_module: Mapped[Optional["Module"]] = relationship(
        remote_side=[id],
        back_populates="child_modules"
    )
    child_modules: Mapped[List["Module"]] = relationship(
        back_populates="parent_module",
        cascade="all, delete-orphan"
    )
    material_usages: Mapped[List["ModuleMaterialUsage"]] = relationship(
        back_populates="module",
        cascade="all, delete-orphan"
    )
    hardware_usages: Mapped[List["ModuleHardwareUsage"]] = relationship(
        back_populates="module",
        cascade="all, delete-orphan"
    )
# TODO Переделать модуль должен быть в составе продукта, фурнитура и оборудование в составе модуля,
#  убрать самореферентную связь.