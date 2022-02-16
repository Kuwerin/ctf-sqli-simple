"""Base Application"""
from typing import NoReturn, Optional

from databases.core import Database
from fastapi import FastAPI
import uvicorn

from settings import AppSettings


class Application:
    repository: Database
    settings: AppSettings
    
    def __init__(
            self, 
            settings: AppSettings,
            ):

        self.settings = settings
        self.repository = Database(self._get_db_uri())

    def _get_db_uri(self) -> str:
        settings = self.settings.repository
        return f"postgresql://{settings.user}:{settings.password}@{settings.host}:5432/{settings.name}"

    def run(self, transport: FastAPI) -> Optional[NoReturn]:
        settings = self.settings.transport
        uvicorn.run(transport, host=settings.host, port=settings.port, debug=True, timeout_keep_alive=0)

settings = AppSettings.load()
application = Application(settings)
