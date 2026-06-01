from pydantic_settings import BaseSettings

# This class is used to load the environment variables from the .env file and make them available as attributes of the Settings class.
class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

# This creates an instance of the Settings class, which will load the environment variables and make them available as attributes.
settings = Settings()