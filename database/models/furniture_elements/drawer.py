from typing import List, Optional
from sqlalchemy import Integer, String, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database.db import Base
from database.models.product import Product


class Drawer(Base):
    __tablename__ = "drawer"

    id: Mapped[int] = mapped_column(primary_key=True)
    module_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("module.id", ondelete="CASCADE"),
        nullable=False
    )
    detail_id: Mapped[int] = mapped_column(
        ForeignKey("detail.id", ondelete="CASCADE"),
        nullable=False
    )