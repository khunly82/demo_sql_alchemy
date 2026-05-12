from __future__ import annotations
from sqlalchemy.orm import  Session, joinedload
from sqlalchemy import select

from models import *

class ProductRepository:
    __session: Session
    def __init__(self, session: Session):
        self.__session = session

    def get_all_with_category(self) -> list[Product]:
        stmt = (
            select(Product)
                .options(joinedload(Product.category))
        )
        return self.__session.scalars(stmt).all()
