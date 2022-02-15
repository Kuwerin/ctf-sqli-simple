from os import environ
import re

from databases import Database

from pydantic_settings import load_settings
from settings import AppSettings
repository_vars= load_settings(AppSettings)

class Config:
    """
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_NAME: str
    """
    
    """
    def __init__(self):
        self.DB_USER = environ.get("DB_USER", "postgres")
        self.DB_PASSWORD = environ.get("DB_PASSWORD", "pgpassword")
        self.DB_HOST = environ.get("DB_HOST", "localhost")

        self.DB_NAME = environ.get("DB_NAME", "postgres")
    """
    def __init__(self):
        self.user = repository_vars.repository.name
        self.password = repository_vars.repository.password
        self.host = repository_vars.repository.host
        self.name = repository_vars.repository.name

    def get_db_uri(self):
        return f"postgresql://{self.user}:{self.repository_vars.password}@{self.repository_vars.host}:5432/{self.repository_vars.name}"


cfg = Config()
cursor = Database(cfg.get_db_uri())
