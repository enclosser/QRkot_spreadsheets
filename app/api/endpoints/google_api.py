from aiogoogle import Aiogoogle
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.core.db import get_async_session
from app.core.google_client import get_service
from app.core.user import current_superuser
from app.crud import charity_project_crud
from app.schemas import GoogleApiReport
from app.services.google_api import (spreadsheets_create,
                                     spreadsheets_update_value,
                                     set_user_permissions)

router = APIRouter()


@router.get(
    '/',
    response_model=List[GoogleApiReport],
    dependencies=[Depends(current_superuser)],
)
async def get_report(
        session: AsyncSession = Depends(get_async_session),
        wrapper_services: Aiogoogle = Depends(get_service)
):
    """Только для суперюзеров.

    Формирует отчёт в гугл-таблице, в которой отображаются закрытые проекты,
    отсортированные по скорости сбора средств — от тех, что закрылись быстрее
    всего, до тех, что долго собирали нужную сумму.
    """
    projects = await charity_project_crud.get_projects_by_completion_rate(session)
    spreadsheetid = await spreadsheets_create(wrapper_services)
    await set_user_permissions(spreadsheetid, wrapper_services)
    report_data = await spreadsheets_update_value(spreadsheetid,
                                                  projects,
                                                  wrapper_services)
    return report_data
