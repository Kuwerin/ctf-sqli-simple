from typing import Optional

from pydantic_settings import BaseSettingsModel

class AppSettings(BaseSettingsModel):
    transport: TransportSettings
    repository: PostgresSettings

class TransportSettings(BaseSettingsModel):                                                                                                                                                               
    host: Optional[str] = "localhost"
    port: Optional[int] = 5000

class PostgresSettings(BaseSettingsModel):
    USER: Optional[str] = "postgres"
    PASSWORD: Optional[str] = "pgpassword"
    HOST: Optional[str] = "localhost"
    NAME: Optional[str] = "postgres"