from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, PositiveInt


INVEST_MIN = 0
MAX_LENGTH = 100
MIN_LENGTH = 1


class CharityProjectBase(BaseModel):
    name: Optional[str] = Field(
        None, min_length=MIN_LENGTH, max_length=MAX_LENGTH
    )
    description: Optional[str] = Field(
        None, min_length=MIN_LENGTH
    )
    full_amount: Optional[PositiveInt] = Field(None)

    class Config:
        extra = Extra.forbid


class CharityProjectCreate(CharityProjectBase):
    name: str = Field(
        ..., min_length=MIN_LENGTH, max_length=MAX_LENGTH
    )
    description: str = Field(..., min_length=MIN_LENGTH)
    full_amount: PositiveInt = Field(...)


class CharityProjectUpdate(CharityProjectBase):
    pass


class CharityProjectDB(CharityProjectCreate):
    id: int
    invested_amount: int = Field(INVEST_MIN)
    fully_invested: bool = Field(False)
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
