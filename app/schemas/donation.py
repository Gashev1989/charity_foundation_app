from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, PositiveInt


INVEST_MIN = 0


class DonationBase(BaseModel):
    full_amount: PositiveInt
    comment: Optional[str]

    class Config:
        extra = Extra.forbid


class DonationCreate(DonationBase):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationDB(DonationCreate):
    id: int
    create_date: datetime
    user_id: int
    invested_amount: int = Field(INVEST_MIN)
    fully_invested: bool = Field(False)
    close_date: Optional[datetime]
