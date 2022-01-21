from fastapi import FastAPI
from result import Ok, Err

from repository import FlagRepo, database
from model import Flag, GetAllFlagsResponse

__all__ = [
        "app",
        ]

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/")
async def create_flag():
    res = await FlagRepo.create_flag()

    match res:
        case Ok(value):
            return {"status": value}
        case Err(err):
            return {"error": err}


@app.get("/", response_model=list[GetAllFlagsResponse])
async def get_all_flags():
    res = await FlagRepo.get_all_flags()
    match res:
        case Ok(value):
            return value
        case Err(err):
            return {"error": err}


@app.get("/{flag_name}", response_model=Flag)
async def get_flag_by_name(flag_name: str):
    # TODO: Add match case
    return await FlagRepo.get_flag_by_name(flag_name)
