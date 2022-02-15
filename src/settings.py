from typing import Optional
from unicodedata import name

from pydantic_settings import BaseSettingsModel


class TransportSettings(BaseSettingsModel):
    host: Optional[str] = "localhost"
    port: Optional[int] = 5000

class RepositorySettings(BaseSettingsModel):
    user: Optional[str] = "postgres"
    password: Optional[str] = "pgpassword"
    host: Optional[str] = "localhost"
    name: Optional[str] = "postgres"

class AppSettings(BaseSettingsModel):
    transport: TransportSettings
    repository: RepositorySettings

    class Config:
        env_prefix = 'APP'