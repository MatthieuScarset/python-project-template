from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API settings
    host: str = Field(default="0.0.0.0", description="API server host")
    port: int = Field(default=8000, description="API server port")
