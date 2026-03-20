from sqlalchemy import Date, Integer, case, cast, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import aliased

from core.database.models.logs import EventTypeOrm, LogOrm, SpaceTypeOrm
from core.database.models.main import CommentOrm, PostOrm, UserOrm
from core.dto.comments_dataset import CommentDatasetDTO
from core.dto.general_dataset import GeneralDatasetDTO
from core.exceptions.exceptions import UserNotFoundHTTPException
from core.log import get_logger

logger = get_logger(__name__)


class DatasetService:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def _get_user_or_raise(self, login: str) -> UserOrm:
        user = (
            await self.session.execute(
                select(UserOrm).where(UserOrm.login == login)
            )
        ).scalar_one_or_none()

        if not user:
            raise UserNotFoundHTTPException()

        return user

    async def get_comment_dataset(self, login: str) -> CommentDatasetDTO:
        logger.info("Fetching comment dataset for login=%s", login)
        await self._get_user_or_raise(login)

        PostAuthor = aliased(UserOrm, name="post_author")
        query = (
            select(
                UserOrm.login.label("user_login"),
                PostOrm.header.label("post_header"),
                PostAuthor.login.label("author_login"),
                func.count(CommentOrm.id).label("comments_count"),
            )
            .select_from(CommentOrm)
            .join(UserOrm, UserOrm.id == CommentOrm.author_id)
            .join(PostOrm, PostOrm.id == CommentOrm.post_id)
            .join(PostAuthor, PostAuthor.id == PostOrm.author_id)
            .where(UserOrm.login == login)
            .group_by(UserOrm.login, PostOrm.header, PostAuthor.login)
        )

        dataset = (await self.session.execute(query)).mappings().all()
        return CommentDatasetDTO(dataset=dataset)

    async def get_general_dataset(self, login: str) -> GeneralDatasetDTO:
        logger.info("Fetching general dataset for login=%s", login)
        await self._get_user_or_raise(login)

        query = (
            select(
                cast(LogOrm.datetime, Date).label("date"),
                func.sum(case((EventTypeOrm.name == "login", 1), else_=0))
                .cast(Integer)
                .label("login_count"),
                func.sum(case((EventTypeOrm.name == "logout", 1), else_=0))
                .cast(Integer)
                .label("logout_count"),
                func.sum(case((SpaceTypeOrm.name == "blog", 1), else_=0))
                .cast(Integer)
                .label("blog_event_count"),
            )
            .select_from(LogOrm)
            .join(EventTypeOrm, EventTypeOrm.id == LogOrm.event_type_id)
            .join(SpaceTypeOrm, SpaceTypeOrm.id == LogOrm.space_type_id)
            .join(UserOrm, UserOrm.id == LogOrm.user_id)
            .where(UserOrm.login == login)
            .group_by(cast(LogOrm.datetime, Date))
        )

        dataset = (await self.session.execute(query)).mappings().all()
        return GeneralDatasetDTO(dataset=dataset)
