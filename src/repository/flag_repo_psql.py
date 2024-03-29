from typing import AsyncGenerator

from result import Result, Ok, Err

from app import application
from model import GetAllFlagsResponse, Flag, CreateFlagRequest


class FlagRepo:
    @classmethod
    async def create_flag(cls, req: CreateFlagRequest) -> Result[Flag, str]:
        cursor = await application.get_db_cursor()
        try:
            await cursor.execute("INSERT INTO flag (name, value) VALUES (%s, %s) RETURNING id", (req.name, req.value))
            user_id: tuple = await cursor.fetchone()
            return Ok(Flag(id=user_id[0], name=req.name, value=req.value, is_private=False))
        except Exception as e:
            return Err(str(e))

    @classmethod
    async def get_all_flags(cls) -> AsyncGenerator[GetAllFlagsResponse, None]:
        cursor = await application.get_db_cursor()
        await cursor.execute("SELECT id, name, is_private FROM flag")

        data: list[tuple] = await cursor.fetchall()

        for record in data:
            yield GetAllFlagsResponse.from_row(record)


    @classmethod
    async def get_flag_by_name(cls, flag_name: str) -> Result[Flag, str]:
        cursor = await application.get_db_cursor()
        try:
            await cursor.execute(f"SELECT * FROM flag WHERE name='{flag_name}' AND is_private=false")
            data = await cursor.fetchone()
            
            flag = Flag.from_row(data)
            
            return Ok(flag) 
        except Exception as e:
            return Err(str(e))
