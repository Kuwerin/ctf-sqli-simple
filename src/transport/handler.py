from asyncio import sleep
from typing import Union

from asyncpg.exceptions import CannotConnectNowError
from fastapi import FastAPI
from result import Ok, Err

from repository import FlagRepo, cursor
from model import Flag, GetAllFlagsResponse, CreateFlagRequest

__all__ = [
        "app",
        ]

app = FastAPI()


@app.on_event("startup")
async def startup():
    try:
        await cursor.connect()
    except (CannotConnectNowError, ConnectionRefusedError):
        await sleep(5)
        await startup()

@app.on_event("shutdown")
async def shutdown():
    await cursor.disconnect()


@app.post("/", response_model=Union[Flag, dict[str, str]])
async def create_flag(flag: CreateFlagRequest):
    res = await FlagRepo.create_flag(flag)
    match res:
        case Ok(value):
            return value
        case Err(err):
            return {"error": err}


@app.get("/", response_model=Union[list[GetAllFlagsResponse], dict[str, str]])
async def get_all_flags():
    res = await FlagRepo.get_all_flags()
    match res:
        case Ok(value):
            return value
        case Err(err):
            return {"error": err}


@app.get("/{flag_name}", response_model=Union[Flag, dict[str, str]])
async def get_flag_by_name(flag_name: str):
    res = await FlagRepo.get_flag_by_name(flag_name)
    match res:
        case Ok(value):
            return value
        case Err(e):
            return {"error": e}

