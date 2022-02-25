"""Base Application"""
from typing import NoReturn, Optional

from aiopg import connect
from aiopg.connection import Connection, Cursor
from fastapi import FastAPI
import uvicorn

from settings import AppSettings


class Application:
    repository: Connection 
    settings: AppSettings
    
    def __init__(
            self, 
            settings: AppSettings,
            ):

        self.settings = settings

    def _get_db_uri(self) -> str:
        settings = self.settings.repository
        return f"postgresql://{settings.user}:{settings.password}@{settings.host}:5432/{settings.database}"

    def run(self, transport: FastAPI) -> Optional[NoReturn]:
        settings = self.settings.transport
        uvicorn.run(transport, host=settings.host, port=settings.port, debug=True, timeout_keep_alive=0)

    async def db_connect(self):
        self.repository = await connect(**self.settings.repository.dict())

    async def db_disconnect(self):
        await self.repository.close()

    async def get_db_cursor(self) -> Cursor:
        return await self.repository.cursor()

settings = AppSettings.load()
application = Application(settings)
