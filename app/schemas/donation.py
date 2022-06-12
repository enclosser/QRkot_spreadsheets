from datetime import datetime
from pydantic import BaseModel, Extra, PositiveInt, UUID4
from typing import Optional


class DonationCreate(BaseModel):
    full_amount: PositiveInt
    comment: Optional[str]

    class Config:
        extra = Extra.forbid


class DonationDB(BaseModel):
    id: int
    user_id: UUID4
    comment: Optional[str]
    full_amount: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
