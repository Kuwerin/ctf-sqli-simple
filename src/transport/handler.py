from fastapi import FastAPI

from src.repository import FlagRepo, database


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/")
async def create_flag():
    # TODO: add duplicate key processing via match case
    await FlagRepo.create_flag()
    return {"status": "created"}


@app.get("/")
async def get_all_flags():
    return await FlagRepo.get_all_flags()


@app.get("/{flag_name}")
async def get_flag_by_name(flag_name: str):
    # TODO: Add match case
    return await FlagRepo.get_flag_by_name(flag_name)
