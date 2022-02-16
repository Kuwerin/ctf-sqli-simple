from typing import Optional
from unicodedata import name

from pydantic_settings import BaseSettingsModel, LoadingError, load_settings


class TransportSettings(BaseSettingsModel):
    host: Optional[str] = "0.0.0.0"
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

    @classmethod
    def load(cls):
        return load_settings(cls=cls, load_env=True)
