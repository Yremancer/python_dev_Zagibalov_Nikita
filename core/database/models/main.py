from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from core.database.database import Base


class UserOrm(Base):
    __tablename__ = "users"
    __table_args__ = {'schema': 'main'}


    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(String(255), unique=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)


class BlogOrm(Base):
    __tablename__ = "blog"
    __table_args__ = {'schema': 'main'}

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)

    owner_id: Mapped[int] = mapped_column(ForeignKey("main.users.id"))


class PostOrm(Base):
    __tablename__ = "post"
    __table_args__ = {'schema': 'main'}

    id: Mapped[int] = mapped_column(primary_key=True)

    header: Mapped[str] = mapped_column(String(255))
    text: Mapped[str] = mapped_column(Text)

    author_id: Mapped[int] = mapped_column(ForeignKey("main.users.id"))
    blog_id: Mapped[int] = mapped_column(ForeignKey("main.blog.id"))


class CommentOrm(Base):
    __tablename__ = "comment"
    __table_args__ = {'schema': 'main'}

    id: Mapped[int] = mapped_column(primary_key=True)

    text: Mapped[str] = mapped_column(Text)

    author_id: Mapped[int] = mapped_column(ForeignKey("main.users.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("main.post.id"))
