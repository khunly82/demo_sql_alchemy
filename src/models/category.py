from __future__ import annotations
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import *

class Category(Base):
    __tablename__ = 'categories'
    category_id: Mapped[int] = mapped_column(primary_key=True)
    category_name: Mapped[str] = mapped_column()
    products: Mapped[list[Product]] = relationship(back_populates='category')