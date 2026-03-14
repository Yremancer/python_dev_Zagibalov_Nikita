from pydantic import BaseModel


class CommentDatasetRow(BaseModel):
    user_login: str
    post_header: str
    author_login: str
    comments_count: int


class CommentDatasetDTO(BaseModel):
    dataset: list[CommentDatasetRow]
