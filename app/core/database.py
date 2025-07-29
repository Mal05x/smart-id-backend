from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLITE_DB = "sqlite:///./student_system.db"
engine = create_engine(SQLITE_DB, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Student Model
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    nfc_uid = Column(String, unique=True)
    name = Column(String)

# Create Tables
Base.metadata.create_all(bind=engine)
