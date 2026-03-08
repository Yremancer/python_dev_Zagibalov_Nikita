from datetime import datetime as dt

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.database.database import BaseLog


class SpaceTypeOrm(BaseLog):
    __tablename__ = "space_type"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


class EventTypeOrm(BaseLog):
    __tablename__ = "event_type"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


class LogOrm(BaseLog):
    __tablename__ = "logs"

    id: Mapped[int] = mapped_column(primary_key=True)
    datetime: Mapped[dt] = mapped_column(DateTime)

    space_type_id: Mapped[int] = mapped_column(ForeignKey("space_type.id"))
    event_type_id: Mapped[int] = mapped_column(ForeignKey("event_type.id"))

    user_id: Mapped[int]
    entity_id: Mapped[int]
