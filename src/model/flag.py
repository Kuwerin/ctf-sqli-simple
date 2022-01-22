from pydantic import BaseModel


class Flag(BaseModel):
    """Flag model"""
    id: int
    name: str
    value: str
    is_private: bool


class GetAllFlagsResponse(BaseModel):
    """Output to get all flags method"""
    id: int
    name: str
    is_private: bool

class CreateFlagRequest(BaseModel):
    """Input to create flag request"""
    name: str
    value: str
