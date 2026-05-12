import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text, Select, func
from sqlalchemy.orm import sessionmaker
from models import Product

load_dotenv()

engine = create_engine(os.getenv('DB_URL'), echo=True)
session_factory = sessionmaker(bind=engine)

with session_factory() as session:
    #select * from products
    #rows = session.query(Product).all()
    stmt = (
        Select(
            Product,
            func.rank().over(
                partition_by=Product.category_id, 
                order_by=Product.unit_price
            ).label('rank_column')
        )#.where(Product.product_name.op('~*')('^b'))
    )
    rows = session.execute(stmt).all()
    for p in rows:
        print(p.Product.product_name, p.rank_column)