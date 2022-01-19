from .postgres import database
from src.model import GetAllFlagsResponse, Flag


class FlagRepo:
    @classmethod
    async def create_flag(cls):
        ...

    @classmethod
    async def get_all_flags(cls) -> GetAllFlagsResponse:
        return await database.fetch_all("SELECT id, name, is_private FROM flag")

    # http://localhost:5000/flag/main-flag' or '1'='1
    @classmethod
    async def get_flag_by_name(cls, flag_name: str) -> Flag:
        return await database.fetch_one(f"SELECT * FROM flag WHERE name='{flag_name}' AND is_private=false")