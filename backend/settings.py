from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str = ""
    langchain_api_key: str = ""

    class Config:
        env_file = "config/.env"

settings = Settings()
