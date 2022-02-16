from os import environ
import re

from databases import Database

from pydantic_settings import load_settings
from settings import AppSettings
repository_vars= load_settings(cls=AppSettings, load_env=True)

class Config:
    def __init__(self):
        self.user = repository_vars.repository.name
        self.password = repository_vars.repository.password
        self.host = repository_vars.repository.host
        self.name = repository_vars.repository.name

    def get_db_uri(self):
        return f"postgresql://{self.user}:{self.password}@{self.host}:5432/{self.name}"


cfg = Config()
cursor = Database(cfg.get_db_uri())
