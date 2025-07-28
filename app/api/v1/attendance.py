from fastapi import APIRouter
router = APIRouter()

@router.post("/nfc-scan")
async def record_attendance(nfc_uid: str):
    return {"status": "Attendance recorded", "nfc_uid": nfc_uid}

