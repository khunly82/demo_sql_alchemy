from __future__ import annotations
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import *


class Product(Base):
    __tablename__ = 'products'
    product_id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column()
    unit_price: Mapped[float] = mapped_column()
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.category_id'))
    category: Mapped[Category] = relationship(back_populates='products')