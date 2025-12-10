from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SCAN_TIMEOUT: int = 15

    class Config:
        env_file = ".env"

settings = Settings()
