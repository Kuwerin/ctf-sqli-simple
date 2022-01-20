from pydantic import BaseModel
from pydantic.fields import Field


class Flag(BaseModel):
    """User's input flag"""
    _id: int
    name: str
    value: str
    is_private: bool


class GetAllFlagsResponse(BaseModel):
    id: int
    name: str
    is_private: bool
