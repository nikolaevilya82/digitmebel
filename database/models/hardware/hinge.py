from sqlalchemy import Integer, String, Enum
from sqlalchemy.orm import Mapped, mapped_column
from database.db import Base


class Hinge(Base):
    __tablename__ = "hinge"
    id: Mapped[int] = mapped_column(primary_key=True)
    brand: Mapped[str] = mapped_column(String(30), nullable=True) # may be nullable=False for all characteristics
    mounting_type: Mapped[str] = mapped_column(
        Enum("накладная", "вкладная", "полунакладная", "other", name="hinge_item_type"),
        nullable=False
    )
    mounting_angle: Mapped[int] = mapped_column(Integer)
    opening_angle: Mapped[int] = mapped_column(Integer)
    color: Mapped[str] = mapped_column(String(30))
    cost: Mapped[int] = mapped_column(Integer)


# TODO Прописать связи.