from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

from sqlalchemy.ext.declarative import declarative_base





SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}'
print("Database ready")

engine = create_engine(SQLALCHEMY_DATABASE_URL)



SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base= declarative_base()




# database Dependency
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()



