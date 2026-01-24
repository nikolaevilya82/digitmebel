from typing import Optional, List
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.db import Base
from database.models.product import Product


class FurnitureType(Base):
    __tablename__ = "furniture_type"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)

    # Связи
    products: Mapped[List["Product"]] = relationship(back_populates="type")