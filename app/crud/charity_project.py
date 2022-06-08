from typing import Dict, List, Optional

from sqlalchemy import extract, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import CRUDBase
from app.models import CharityProject


class CRUDMeetingRoom():    # для тестов
    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession
    ) -> List[Dict[str, str]]:
        projects = await session.execute(
            select(
                CharityProject).where(
                CharityProject.fully_invested).order_by(
                extract('year', CharityProject.close_date) - extract(
                    'year', CharityProject.create_date),
                extract('month', CharityProject.close_date) - extract(
                    'month', CharityProject.create_date),
                extract('day', CharityProject.close_date) - extract(
                    'day', CharityProject.create_date),
            ))
        return projects


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
    ) -> List[Dict[str, str]]:
        response_list = []
        projects = await session.execute(
            select(
                CharityProject).where(
                CharityProject.fully_invested).order_by(
                extract('year', CharityProject.close_date) - extract(
                    'year', CharityProject.create_date),
                extract('month', CharityProject.close_date) - extract(
                    'month', CharityProject.create_date),
                extract('day', CharityProject.close_date) - extract(
                    'day', CharityProject.create_date),
            ))
        projects = projects.scalars().all()
        for project in projects:
            response_list.append(
                {
                    "name": project.name,
                    "collection_time": str(
                        project.close_date - project.create_date
                    ),
                    "description": project.description
                }
            )
        return response_list


charity_project_crud = CRUDCharityProject(CharityProject)
