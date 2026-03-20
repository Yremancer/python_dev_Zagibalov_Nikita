from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.api.responses import responses
from core.database.database import get_async_session
from core.dto.comments_dataset import CommentDatasetDTO
from core.dto.general_dataset import GeneralDatasetDTO
from core.services.dataset_service import DatasetService

dataset_router = APIRouter(tags=["Dataset"])


@dataset_router.get(
    path="/comments",
    status_code=200,
    summary="Возвращает датасет комментариев пользователя",
    response_model=CommentDatasetDTO,
    responses={
        **responses["404_user_not_found"],
        **responses["500_internal_error"],
    },
)
async def get_comment_dataset(
    login: str,
    session: AsyncSession = Depends(get_async_session),
):
    service = DatasetService(session=session)
    return await service.get_comment_dataset(login=login)


@dataset_router.get(
    path="/general",
    status_code=200,
    summary="Возвращает датасет общей информации о действиях пользователя",
    response_model=GeneralDatasetDTO,
    responses={
        **responses["404_user_not_found"],
        **responses["500_internal_error"],
    },
)
async def get_general_dataset(
    login: str,
    session: AsyncSession = Depends(get_async_session),
):
    service = DatasetService(session=session)
    return await service.get_general_dataset(login=login)
