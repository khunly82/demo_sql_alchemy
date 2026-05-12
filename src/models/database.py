from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

class Base(DeclarativeBase, MappedAsDataclass):
    pass

engine = create_engine(os.getenv('DB_URL'), echo=True)

def Session():
    return sessionmaker(bind=engine)()