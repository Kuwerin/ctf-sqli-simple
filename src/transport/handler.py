from asyncio import sleep
from typing import Union

from asyncpg.exceptions import CannotConnectNowError
from fastapi import FastAPI
from result import Ok, Err

from repository import FlagRepo
from model import Flag, GetAllFlagsResponse, CreateFlagRequest
from app import application

__all__ = [
        "transport",
        ]

transport = FastAPI()

@transport.on_event("startup")
async def startup():
    try:
        await application.db_connect()
    except (CannotConnectNowError, ConnectionRefusedError):
        await sleep(5)
        await startup()

@transport.on_event("shutdown")
async def shutdown():
    await application.db_disconnect()


@transport.post("/", response_model=Union[Flag, dict[str, str]])
async def create_flag(flag: CreateFlagRequest):
    res = await FlagRepo.create_flag(flag)
    match res:
        case Ok(value):
            return value
        case Err(err):
            return {"error": err}


@transport.get("/", response_model=list[GetAllFlagsResponse])
async def get_all_flags():
    return [result async for result in FlagRepo.get_all_flags()]


@transport.get("/{flag_name}", response_model=Union[Flag, dict[str, str]])
async def get_flag_by_name(flag_name: str):
    res = await FlagRepo.get_flag_by_name(flag_name)
    match res:
        case Ok(value):
            return value
        case Err(e):
            return {"error": e}

