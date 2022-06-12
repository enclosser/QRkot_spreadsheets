from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.api.services import get_investment
from app.api.validators import (check_name_duplicate,
                                check_not_less_than_invested,
                                check_project_exists_and_not_fully_invested,
                                check_project_not_invested)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud import charity_project_crud
from app.schemas import (CharityProjectCreate,
                         CharityProjectDB,
                         CharityProjectUpdate)


router = APIRouter()


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)]
)
async def create_new_charity_project(
        charity_project: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров."""
    await check_name_duplicate(charity_project.name, session)
    new_project = await charity_project_crud.create(charity_project, session)
    await session.refresh(new_project)
    new_project = await get_investment(new_project, session)
    return new_project


@router.get(
    '/',
    response_model=List[CharityProjectDB],
    response_model_exclude_none=True
)
async def get_all_charity_projects(
        session: AsyncSession = Depends(get_async_session),
):
    all_projects = await charity_project_crud.get_multi(session)
    return all_projects


@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)]
)
async def update_charity_project(
        project_id: int,
        obj_in: CharityProjectUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров."""
    project = await check_project_exists_and_not_fully_invested(
        project_id,
        session
    )
    if obj_in.name is not None:
        await check_name_duplicate(obj_in.name, session)
    if obj_in.full_amount is not None:
        await check_not_less_than_invested(project, obj_in.full_amount)
    project = await charity_project_crud.update(
        db_obj=project,
        obj_in=obj_in,
        session=session,
    )
    project = await charity_project_crud.check_invested_amount(project, session)
    return project


@router.delete(
    '/{project_id}',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)]
)
async def remove_charity_project(
        project_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров."""
    project = await check_project_exists_and_not_fully_invested(
        project_id,
        session
    )
    project = await check_project_not_invested(project, session)
    project = await charity_project_crud.remove(project, session)
    return project
