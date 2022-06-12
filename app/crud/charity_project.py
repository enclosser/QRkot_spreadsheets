from sqlalchemy import select, extract
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional

from app.crud import CRUDBase
from app.models import CharityProject
from app.schemas import CharityProjectDB


class CRUDCharityProject(CRUDBase):

    async def get_project_id_by_name(
            self,
            project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        db_project_id = db_project_id.scalars().first()
        return db_project_id

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession
    ) -> List[CharityProjectDB]:
        projects = await session.execute(
            select(
                CharityProject).where(
                CharityProject.fully_invested).order_by(
                    extract('year', CharityProject.close_date) -
                    extract('year', CharityProject.create_date),
                    extract('month', CharityProject.close_date) -
                    extract('month', CharityProject.create_date),
                    extract('day', CharityProject.close_date) -
                    extract('day', CharityProject.create_date)
            )
        )
        projects = projects.scalars().all()
        return projects


charity_project_crud = CRUDCharityProject(CharityProject)
