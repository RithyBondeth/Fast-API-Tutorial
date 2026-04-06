from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings powered by Pydantic.
    It automatically reads from your .env file and validates the data types.
    """

    MONGO_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    LOG_LEVEL: str = "INFO"

    # This special config tells Pydantic to look for a .env file
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


# We create a single instance of settings to be used throughout the app
settings = Settings()