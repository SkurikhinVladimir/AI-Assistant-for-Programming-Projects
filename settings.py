from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_name: str
    api_base: str
    api_key: str

    class Config:
        env_file = ".env"

settings = Settings()
