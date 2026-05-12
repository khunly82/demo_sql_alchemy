from models import Session
from repositories import ProductRepository
from models import *
Base.metadata.create_all(bind=engine)

with Session() as session:
    product_repository = ProductRepository(session)
    for p in product_repository.get_all_with_category():
        print(p.product_name, p.category.category_name)