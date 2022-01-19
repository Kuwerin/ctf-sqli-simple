from os import environ

from databases import Database


class Config:
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_NAME: str

    def __init__(self):
        self.DB_USER = environ.get("DB_USER", "postgres")
        self.DB_PASSWORD = environ.get("DB_PASSWORD", "pgpassword")
        self.DB_HOST = environ.get("DB_HOST", "localhost")

        self.DB_NAME = environ.get("DB_NAME", "pgdb")

    def get_db_uri(self):
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:5432/{self.DB_NAME}"


cfg = Config()
database = Database(cfg.get_db_uri())
