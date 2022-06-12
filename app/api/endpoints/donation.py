from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.api.services import make_investment
from app.core.db import get_async_session
from app.core.user import current_user, current_superuser
from app.crud import donation_crud
from app.schemas import DonationCreate, DonationDB, UserDB


router = APIRouter()


@router.post(
    '/',
    response_model=DonationDB,
    response_model_exclude_none=True,
    response_model_exclude={
        'user_id',
        'invested_amount',
        'fully_invested',
        'close_date'
    }
)
async def create_new_donation(
        donation: DonationCreate,
        session: AsyncSession = Depends(get_async_session),
        user: UserDB = Depends(current_user)
):
    new_donation = await donation_crud.create(donation, session, user)
    await session.refresh(new_donation)
    new_donation = await make_investment(new_donation, session)
    return new_donation


@router.get(
    '/',
    response_model=List[DonationDB],
    dependencies=[Depends(current_superuser)]

)
async def get_all_donations(
        session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров."""
    all_donations = await donation_crud.get_multi(session)
    return all_donations


@router.get(
    '/my',
    response_model=List[DonationDB],
    response_model_exclude={
        'user_id',
        'invested_amount',
        'fully_invested',
        'close_date'
    }
)
async def get_all_donations(
        session: AsyncSession = Depends(get_async_session),
        user: UserDB = Depends(current_user)
):
    current_user_donations = await donation_crud.get_by_user(session, user)
    return current_user_donations
