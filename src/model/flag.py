from pydantic import BaseModel


class Flag(BaseModel):
    """Flag model"""
    id: int
    name: str
    value: str
    is_private: bool

    @classmethod
    def from_row(cls, row: tuple):
        if not row:
            raise Exception(f"no public flags with that name in a repository")

        return Flag(
                id=row[0],
                name=row[1],
                value=row[2],
                is_private=row[3],
                )


class GetAllFlagsResponse(BaseModel):
    """Output to get all flags method"""
    id: int
    name: str
    is_private: bool

    @classmethod
    def from_row(cls, row: tuple):
        return GetAllFlagsResponse(
                id=row[0],
                name=row[1],
                is_private=row[2],
                )

class CreateFlagRequest(BaseModel):
    """Input to create flag request"""
    name: str
    value: str

    @classmethod
    def from_row(cls, row: tuple):
        return CreateFlagRequest(
                name=row[0],
                value=row[1],
                )

