from databases.backends.postgres import Record
from result import Result, Ok, Err

from .postgres import database
from model import GetAllFlagsResponse, Flag


class FlagRepo:
    @classmethod
    async def create_flag(cls) -> Result[Flag, str]:
        try:
            await database.execute("INSERT INTO flag (name, flag) VALUES ('tester', 'tested')")
            return Ok(Flag(_id=0, name="tester", value="tested", is_private=False))
        except Exception as e:
            return Err(str(e))

    @classmethod
    async def get_all_flags(cls) -> Result[list[GetAllFlagsResponse], str]:
        try:
            data: list[Record] = await database.fetch_all("SELECT id, name, is_private FROM flag")
            flags: list[GetAllFlagsResponse] = []
            # TODO: try use list comprehensions
            for record in data:
                kwargs = dict(zip(record.keys(), record.values()))
                flags.append(GetAllFlagsResponse(**kwargs))
            return Ok(flags)
        except Exception as e:
            return Err(str(e))

    # http://localhost:5000/flag/main-flag' or '1'='1
    @classmethod
    async def get_flag_by_name(cls, flag_name: str) -> Flag:
        return await database.fetch_one(f"SELECT * FROM flag WHERE name='{flag_name}' AND is_private=false")
