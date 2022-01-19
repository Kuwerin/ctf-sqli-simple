from pydantic import BaseModel


class Flag(BaseModel):
    """User's input flag"""
    _id: int
    name: str
    flag: str
    is_private: bool
