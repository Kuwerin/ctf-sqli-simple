from .postgres import database
from result import Result, Ok, Err

from src.model import GetAllFlagsResponse, Flag


class FlagRepo:
    @classmethod
    async def create_flag(cls) -> Result[Flag, str]:
        try:
            await database.execute("INSERT INTO flag (name, flag) VALUES ('tester', 'tested')")
            return Ok(Flag(_id=0, name="tester", value="tested", is_private=False))
        except Exception as e:
            return Err(str(e))

    @classmethod
    async def get_all_flags(cls) -> GetAllFlagsResponse:
        return await database.fetch_all("SELECT id, name, is_private FROM flag")

    # http://localhost:5000/flag/main-flag' or '1'='1
    @classmethod
    async def get_flag_by_name(cls, flag_name: str) -> Flag:
        return await database.fetch_one(f"SELECT * FROM flag WHERE name='{flag_name}' AND is_private=false")
