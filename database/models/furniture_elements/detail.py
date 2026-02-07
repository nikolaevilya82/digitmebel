from typing import Optional
from sqlalchemy import Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database.db import Base
from database.models.furniture_elements.module import Module
from database.models.furniture_elements.sheet_material import SheetMaterial


class Detail(Base):
    __tablename__ = "detail"
    id: Mapped[int] = mapped_column(primary_key=True)
    module_id: Mapped[int] = mapped_column(
        ForeignKey("module.id", ondelete="CASCADE"),
        nullable=False
    )
    sheet_material_id: Mapped[int] = mapped_column(ForeignKey(
        "sheet_material.id", ondelete="CASCADE"),
        nullable=False
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    width: Mapped[int] = mapped_column(Integer, nullable=False)  # в мм
    height: Mapped[int] = mapped_column(Integer, nullable=False)
    depth: Mapped[int] = mapped_column(Integer, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, default=1)
    placement_data: Mapped[Optional[dict]] = mapped_column(JSON)

    # связи
    project: Mapped["Module"] = relationship(back_populates="detail")
    sheet_material: Mapped["SheetMaterial"] = relationship(back_populates="sheet_material")