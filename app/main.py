from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, Student
from pydantic import BaseModel
from app.core.database import SessionLocal
from app.core.models.student import Student

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic Model for NFC Request
class NFCRequest(BaseModel):
    nfc_uid: str

# API Endpoint
@app.post("/api/nfc/auth")
async def nfc_auth(request: NFCRequest, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.nfc_uid == request.nfc_uid).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"student_id": student.id, "name": student.name}
