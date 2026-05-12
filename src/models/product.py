from models import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Product(Base):
    __tablename__ = 'products'
    product_id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column()
    unit_price: Mapped[float] = mapped_column()
    category_id: Mapped[int] = mapped_column()