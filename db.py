from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from config import MYSQL_URL



engine = create_engine(MYSQL_URL)
Base = declarative_base()
session = sessionmaker(bind=engine, autoflush=True)


def get_session():
    return session()