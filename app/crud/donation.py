from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Donation
from app.schemas import UserDB


class CRUDDonation(CRUDBase):

    async def get_by_user(
            self,
            session: AsyncSession,
            user: UserDB
    ):
        donations = await session.execute(select(Donation).where(
            Donation.user_id == user.id,
        )
        )
        donations = donations.scalars().all()
        return donations


donation_crud = CRUDDonation(Donation)
