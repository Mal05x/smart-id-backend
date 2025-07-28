from fastapi import FastAPI
from app.api.v1 import api_router

app = FastAPI(title="Smart Student ID System")
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"status": "API is running"}

