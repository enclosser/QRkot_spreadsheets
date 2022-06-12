from datetime import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CharityProject, Donation


def set_full_invested_fields(obj):
    obj.invested_amount = obj.full_amount
    obj.fully_invested = 1
    obj.close_date = datetime.now()
    return obj


async def make_investment(
        donation,
        session: AsyncSession
):
    result = await session.execute(select(
        CharityProject).where(
        CharityProject.fully_invested == 0).order_by(
        CharityProject.create_date)
    )
    projects = result.scalars().all()
    donation_balance = donation.full_amount - donation.invested_amount
    for project in projects:
        amount_required = project.full_amount - project.invested_amount
        if donation_balance < amount_required:
            project.invested_amount += donation_balance
            donation = set_full_invested_fields(donation)
            session.add(project)
            break

        if donation_balance == amount_required:
            donation = set_full_invested_fields(donation)
            project = set_full_invested_fields(project)
            session.add(project)
            break

        if donation_balance > amount_required:
            project = set_full_invested_fields(project)
            donation.invested_amount += amount_required
            donation_balance -= amount_required
            session.add(project)

    session.add(donation)
    await session.commit()
    await session.refresh(donation)
    return donation


async def get_investment(
        project,
        session: AsyncSession
):
    result = await session.execute(select(Donation).where(
        Donation.fully_invested == 0).order_by(
        Donation.create_date)
    )
    donations = result.scalars().all()
    amount_required = project.full_amount - project.invested_amount
    for donation in donations:
        donation_balance = donation.full_amount - donation.invested_amount
        if donation_balance < amount_required:
            project.invested_amount += donation_balance
            donation = set_full_invested_fields(donation)
            session.add(donation)
            amount_required -= donation_balance
            continue

        if donation_balance == amount_required:
            project = set_full_invested_fields(project)
            donation = set_full_invested_fields(donation)
            session.add(donation)
            break

        if donation_balance > amount_required:
            project = set_full_invested_fields(project)
            donation.invested_amount += amount_required
            session.add(donation)
            break

    session.add(project)
    await session.commit()
    await session.refresh(project)
    return project
