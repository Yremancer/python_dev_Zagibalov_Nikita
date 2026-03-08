from typing import Optional

from fastapi import APIRouter

from core.api.responces import responses
from core.dto.comments_dataset import CommentDatasetDTO, GeneralDatasetDTO

dataset_router = APIRouter()


@dataset_router.get(
    path="/comment",
    status_code=200,
    summary="Возвращает датасет комментариев пользователей",
    response_model=CommentDatasetDTO,
    responses={
        **responses["404_user_not_found"],
        **responses["500_internal_error"],
    },
)
async def get_comment_dataset(login: Optional[str] = None):
    pass


@dataset_router.get(
    path="/general",
    status_code=200,
    summary="Возвращает датасет общей информации о дейсвтиях пользователей",
    response_model=GeneralDatasetDTO,
    responses={
        **responses["404_user_not_found"],
        **responses["500_internal_error"],
    },
)
async def get_general_dataset(login: Optional[str] = None):
    pass
