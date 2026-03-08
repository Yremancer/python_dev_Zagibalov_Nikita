from datetime import date

from pydantic import BaseModel


class CommentDatasetRow(BaseModel):
    user_login: str
    post_header: str
    author_login: str
    comments_count: int


class CommentDatasetDTO(BaseModel):
    dataset: list[CommentDatasetRow]


class GeneralDatasetRow(BaseModel):
    data: date
    login_count: int
    logout_count: int
    blog_event_conut: int


class GeneralDatasetDTO(BaseModel):
    dataset: list[GeneralDatasetRow]
