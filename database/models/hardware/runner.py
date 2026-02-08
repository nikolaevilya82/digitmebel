from typing import List, Optional
from sqlalchemy import Column, Integer, String, ForeignKey, BOOLEAN, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database.db import Base


class Runner(Base):
    __tablename__ = "runner"
    id: Mapped[int] = mapped_column(primary_key=True)
    brand: Mapped[str] = mapped_column(String(30))
    item_type: Mapped[str] = mapped_column(
        Enum("скрытый монтаж", "шариковые", "метабоксы", "other",
             name="runner_item_type"),
        nullable=False
    )
    cost: Mapped[int] = mapped_column(Integer)
    depth: Mapped[int] = mapped_column(Integer, nullable=False)
    height: Mapped[int] = mapped_column(Integer, nullable=True)
    closing_type: Mapped[str] = mapped_column(
        Enum("soft close", "manual close", "push-to-open", "other",
             name="runner_closing_type"),
        nullable=False
    )
    extension_type: Mapped[str] = mapped_column(
        Enum("partial", "full", name="runner_extension_type"),
        nullable=False
    )
    drawer_id: Mapped[int] = mapped_column(ForeignKey(
        "drawer_id", ondelete="CASCADE"),
        nullable=False
    )

# TODO Написать связи: drawer, module.