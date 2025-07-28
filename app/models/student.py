from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True)
    student_id = Column(String, unique=True)
    nfc_uid = Column(String, unique=True)

