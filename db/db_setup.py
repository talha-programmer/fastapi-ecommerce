from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:password@localhost/sample_ecommerce"


engine = create_engine(SQLALCHEMY_DATABASE_URL, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)


Base = declarative_base()


# DB Utilities
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
