from distutils.log import debug
from typing import Optional

from pydantic_settings import BaseSettingsModel

class AppSettings(BaseSettingsModel):
    transport: TransportSettings
    postgres: PostgresSettings

class TransportSettings(BaseSettingsModel):                                                                                                                                                               
    host: Optional[str] = "localhost"
    port: Optional[int] = 5000

class PostgresSettings(BaseSettingsModel):
    DB_USER: Optional[str]
    DB_PASSWORD: Optional[str]
    DB_HOST: Optional[str]
    DB_NAME: Optional[str]