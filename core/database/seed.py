from datetime import datetime

from sqlalchemy import select

from core.database.database import async_session_maker
from core.database.models.logs import EventTypeOrm, LogOrm, SpaceTypeOrm
from core.database.models.main import BlogOrm, CommentOrm, PostOrm, UserOrm
from core.log import get_logger

logger = get_logger(__name__)


async def seed_main_db():
    async with async_session_maker() as session:
        result = await session.execute(select(UserOrm).limit(1))
        if result.scalar_one_or_none() is not None:
            return

    async with async_session_maker() as session:
        async with session.begin():
            alice = UserOrm(id=1, login="alice", email="alice@example.com")
            bob = UserOrm(id=2, login="bob", email="bob@example.com")
            charlie = UserOrm(
                id=3, login="charlie", email="charlie@example.com"
            )
            session.add_all([alice, bob, charlie])
            await session.flush()

            blog_alice = BlogOrm(
                id=1,
                name="Alice's Blog",
                description="Блог Алисы о технологиях",
                owner_id=1,
            )
            blog_bob = BlogOrm(
                id=2,
                name="Bob's Blog",
                description="Блог Боба о путешествиях",
                owner_id=2,
            )
            session.add_all([blog_alice, blog_bob])
            await session.flush()

            post1 = PostOrm(
                id=1,
                header="Python Tips",
                text="Полезные советы по Python",
                author_id=1,
                blog_id=1,
            )
            post2 = PostOrm(
                id=2,
                header="Travel Guide",
                text="Гайд по путешествиям",
                author_id=2,
                blog_id=2,
            )
            post3 = PostOrm(
                id=3,
                header="SQLAlchemy Basics",
                text="Основы SQLAlchemy",
                author_id=1,
                blog_id=1,
            )
            session.add_all([post1, post2, post3])
            await session.flush()

            comments = [
                CommentOrm(text="Отличная статья!", author_id=2, post_id=1),
                CommentOrm(
                    text="Спасибо, очень полезно", author_id=2, post_id=1
                ),
                CommentOrm(text="Жду продолжения", author_id=2, post_id=3),
                CommentOrm(text="Круто!", author_id=3, post_id=1),
                CommentOrm(text="Хочу в путешествие", author_id=3, post_id=2),
                CommentOrm(text="Интересно", author_id=3, post_id=2),
                CommentOrm(
                    text="Полезно для новичков", author_id=3, post_id=3
                ),
                CommentOrm(text="Классный гайд!", author_id=1, post_id=2),
            ]
            session.add_all(comments)
    logger.info("Main DB seeded")


async def seed_logs_db():
    async with async_session_maker() as session:
        result = await session.execute(select(SpaceTypeOrm).limit(1))
        if result.scalar_one_or_none() is not None:
            return

    async with async_session_maker() as session:
        async with session.begin():
            space_global = SpaceTypeOrm(id=1, name="global")
            space_blog = SpaceTypeOrm(id=2, name="blog")
            space_post = SpaceTypeOrm(id=3, name="post")
            session.add_all([space_global, space_blog, space_post])
            await session.flush()

            evt_login = EventTypeOrm(id=1, name="login")
            evt_comment = EventTypeOrm(id=2, name="comment")
            evt_create_post = EventTypeOrm(id=3, name="create_post")
            evt_delete_post = EventTypeOrm(id=4, name="delete_post")
            evt_logout = EventTypeOrm(id=5, name="logout")
            session.add_all(
                [
                    evt_login,
                    evt_comment,
                    evt_create_post,
                    evt_delete_post,
                    evt_logout,
                ]
            )
            await session.flush()

            logs = [
                LogOrm(
                    datetime=datetime(2025, 1, 15, 9, 0),
                    user_id=1,
                    space_type_id=1,
                    event_type_id=1,
                    entity_id=0,
                ),
                LogOrm(
                    datetime=datetime(2025, 1, 15, 10, 0),
                    user_id=1,
                    space_type_id=2,
                    event_type_id=3,
                    entity_id=1,
                ),
                LogOrm(
                    datetime=datetime(2025, 1, 15, 11, 0),
                    user_id=1,
                    space_type_id=3,
                    event_type_id=2,
                    entity_id=2,
                ),
                LogOrm(
                    datetime=datetime(2025, 1, 15, 18, 0),
                    user_id=1,
                    space_type_id=1,
                    event_type_id=5,
                    entity_id=0,
                ),
                LogOrm(
                    datetime=datetime(2025, 1, 15, 8, 0),
                    user_id=2,
                    space_type_id=1,
                    event_type_id=1,
                    entity_id=0,
                ),
                LogOrm(
                    datetime=datetime(2025, 1, 15, 12, 0),
                    user_id=2,
                    space_type_id=3,
                    event_type_id=2,
                    entity_id=1,
                ),
                LogOrm(
                    datetime=datetime(2025, 1, 15, 13, 0),
                    user_id=2,
                    space_type_id=3,
                    event_type_id=2,
                    entity_id=1,
                ),
                LogOrm(
                    datetime=datetime(2025, 1, 15, 20, 0),
                    user_id=2,
                    space_type_id=1,
                    event_type_id=5,
                    entity_id=0,
                ),
                LogOrm(
                    datetime=datetime(2025, 1, 15, 14, 0),
                    user_id=3,
                    space_type_id=1,
                    event_type_id=1,
                    entity_id=0,
                ),
                LogOrm(
                    datetime=datetime(2025, 1, 15, 15, 0),
                    user_id=3,
                    space_type_id=3,
                    event_type_id=2,
                    entity_id=1,
                ),
                LogOrm(
                    datetime=datetime(2025, 1, 15, 19, 0),
                    user_id=3,
                    space_type_id=1,
                    event_type_id=5,
                    entity_id=0,
                ),
                LogOrm(
                    datetime=datetime(2025, 1, 16, 9, 0),
                    user_id=1,
                    space_type_id=1,
                    event_type_id=1,
                    entity_id=0,
                ),
                LogOrm(
                    datetime=datetime(2025, 1, 16, 10, 0),
                    user_id=1,
                    space_type_id=2,
                    event_type_id=3,
                    entity_id=1,
                ),
                LogOrm(
                    datetime=datetime(2025, 1, 16, 17, 0),
                    user_id=1,
                    space_type_id=1,
                    event_type_id=5,
                    entity_id=0,
                ),
                LogOrm(
                    datetime=datetime(2025, 1, 16, 10, 0),
                    user_id=2,
                    space_type_id=1,
                    event_type_id=1,
                    entity_id=0,
                ),
                LogOrm(
                    datetime=datetime(2025, 1, 16, 11, 0),
                    user_id=2,
                    space_type_id=3,
                    event_type_id=2,
                    entity_id=3,
                ),
                LogOrm(
                    datetime=datetime(2025, 1, 16, 12, 0),
                    user_id=2,
                    space_type_id=2,
                    event_type_id=3,
                    entity_id=2,
                ),
                LogOrm(
                    datetime=datetime(2025, 1, 16, 13, 0),
                    user_id=2,
                    space_type_id=2,
                    event_type_id=4,
                    entity_id=2,
                ),
                LogOrm(
                    datetime=datetime(2025, 1, 16, 21, 0),
                    user_id=2,
                    space_type_id=1,
                    event_type_id=5,
                    entity_id=0,
                ),
                LogOrm(
                    datetime=datetime(2025, 1, 16, 8, 0),
                    user_id=3,
                    space_type_id=1,
                    event_type_id=1,
                    entity_id=0,
                ),
                LogOrm(
                    datetime=datetime(2025, 1, 16, 9, 0),
                    user_id=3,
                    space_type_id=1,
                    event_type_id=1,
                    entity_id=0,
                ),
                LogOrm(
                    datetime=datetime(2025, 1, 16, 10, 0),
                    user_id=3,
                    space_type_id=3,
                    event_type_id=2,
                    entity_id=1,
                ),
                LogOrm(
                    datetime=datetime(2025, 1, 16, 11, 0),
                    user_id=3,
                    space_type_id=3,
                    event_type_id=2,
                    entity_id=2,
                ),
                LogOrm(
                    datetime=datetime(2025, 1, 16, 12, 0),
                    user_id=3,
                    space_type_id=3,
                    event_type_id=2,
                    entity_id=3,
                ),
                LogOrm(
                    datetime=datetime(2025, 1, 16, 22, 0),
                    user_id=3,
                    space_type_id=1,
                    event_type_id=5,
                    entity_id=0,
                ),
            ]
            session.add_all(logs)
    logger.info("Logs DB seeded")


async def seed_all():
    await seed_main_db()
    await seed_logs_db()
