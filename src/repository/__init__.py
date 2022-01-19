__all__ = [
    "database",
    "FlagRepo",
]

from .flag_repo_psql import FlagRepo
from .postgres import database
