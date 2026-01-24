from typing import List, Optional
from sqlalchemy import Column, Integer, String, ForeignKey, BOOLEAN
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database.db import Base


class SheetMaterial(Base):
    __tablename__ = "sheet_materials"
    id: Mapped[int] = mapped_column(primary_key=True)
    color: Mapped[str] = mapped_column(String(50))
    brand: Mapped[str] = mapped_column(String(50), nullable=True)
    thickness: Mapped[int] = mapped_column(Integer)
    width: Mapped[int] = mapped_column(Integer)
    height: Mapped[int] = mapped_column(Integer)
    rotation: Mapped[bool] = mapped_column(BOOLEAN)

