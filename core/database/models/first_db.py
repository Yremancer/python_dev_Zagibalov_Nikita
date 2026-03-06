from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from sqlalchemy import ForeignKey


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)


class Blog(Base):
    __tablename__ = "blog"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str]
    description: Mapped[str]

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))


class Post(Base):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(primary_key=True)

    header: Mapped[str]
    text: Mapped[str]

    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    blog_id: Mapped[int] = mapped_column(ForeignKey("blog.id"))


class Comment(Base):
    __tablename__ = "comment"

    id: Mapped[int] = mapped_column(primary_key=True)

    text: Mapped[str]

    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))