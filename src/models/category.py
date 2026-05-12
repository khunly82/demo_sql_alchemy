from models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models import Product


class Category(Base):
    __tablename__ = 'categories'
    category_id: Mapped[int] = mapped_column(primary_key=True)
    category_name: Mapped[str] = mapped_column()
    products: Mapped[list['Product']] = relationship(back_populates='category')