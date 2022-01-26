from typing import Sequence
from databases.backends.postgres import Record
from result import Result, Ok, Err

from .postgres import cursor
from model import GetAllFlagsResponse, Flag, CreateFlagRequest


class FlagRepo:
    @classmethod
    async def create_flag(cls, req: CreateFlagRequest) -> Result[Flag, str]:
        try:
            user_id = await cursor.execute("INSERT INTO flag (name, flag) VALUES (:name, :value) RETURNING id", req.dict())
            return Ok(Flag(id=user_id, name=req.name, value=req.value, is_private=False))
        except Exception as e:
            return Err(str(e))

    @classmethod
    async def get_all_flags(cls) -> Result[list[GetAllFlagsResponse], str]:
        try:
            data: list[Record | Sequence] = await cursor.fetch_all("SELECT id, name, is_private FROM flag")

            flags: list[GetAllFlagsResponse] = []

            flags = [(GetAllFlagsResponse(**(dict(zip(record.keys(), record.values()))))) for record in data]
            return Ok(flags)
        except Exception as e:
            return Err(str(e))

    @classmethod
    async def get_flag_by_name(cls, flag_name: str) -> Result[Flag, str]:
        try:
            flag = await cursor.fetch_one(f"SELECT * FROM flag WHERE name='{flag_name}' AND is_private=false")
            match flag:
                case Flag(flag):
                    return Ok(flag)
                case None:
                    raise Exception("no public flags in database")

            return Ok(flag)
        except Exception as e:
            return Err(str(e))
