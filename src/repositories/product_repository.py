from sqlalchemy.orm import Session, joinedload
from sqlalchemy import Select
from models import Product

class ProductRepository:
    __session: Session
    def __init__(self, session: Session):
        self.__session = session

    def get_all_with_category(self) -> list['Product']:
        stmt = (
            Select(Product)
                .options(joinedload(Product.category))
        )
        return self.__session.scalars(stmt).all()
