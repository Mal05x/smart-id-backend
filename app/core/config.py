from pydantic import BaseSettings

class Settings(BaseSettings):
    POSTGRES_URL: str = "postgresql://postgres:postgres@db:5432/smartid"
    SECRET_KEY: str = "302005"
    
    class Config:
        env_file = ".env"

settings = Settings()

