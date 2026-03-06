from sqlalchemy.orm import Mapped, mapped_column
from database import BaseLog
from sqlalchemy import ForeignKey, DateTime
from datetime import datetime as dt


class SpaceType(BaseLog):
    __tablename__ = "space_type"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


class EventType(BaseLog):
    __tablename__ = "event_type"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


class Log(BaseLog):
    __tablename__ = "logs"

    id: Mapped[int] = mapped_column(primary_key=True)
    datetime: Mapped[dt] = mapped_column(DateTime)

    space_type_id: Mapped[int] = mapped_column(ForeignKey("space_type.id"))
    event_type_id: Mapped[int] = mapped_column(ForeignKey("event_type.id"))

    user_id: Mapped[int]
    entity_id
    