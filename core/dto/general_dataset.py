from datetime import date

from pydantic import BaseModel


class GeneralDatasetRow(BaseModel):
    date: date
    login_count: int
    logout_count: int
    blog_event_count: int


class GeneralDatasetDTO(BaseModel):
    dataset: list[GeneralDatasetRow]
