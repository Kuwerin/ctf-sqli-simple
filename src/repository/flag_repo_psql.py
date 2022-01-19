from .postgres import database


class FlagRepo:
    @classmethod
    async def create_flag():
        ...

    @classmethod
    async def get_all_flags():
        return await database.fetch_all("SELECT (id, name, is_private) FROM flag")

    # http://localhost:5000/flag/main-flag' or '1'='1
    @classmethod
    async def get_flag_by_name(flag_name: str):
        return await database.fetch_one(f"SELECT * FROM flag WHERE name='{flag_name}' AND is_private=false")