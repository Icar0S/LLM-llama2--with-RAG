from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    API_HOST: str = "localhost"
    API_PORT: int = 8000

    CHROMA_PATH: str = "../../chroma"
    DATA_PATH: str = "../../data/"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

settings = Config()
