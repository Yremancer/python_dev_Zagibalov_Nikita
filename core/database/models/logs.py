from datetime import datetime as dt

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from core.database.database import Base


class SpaceTypeOrm(Base):
    __tablename__ = "space_type"
    __table_args__ = {"schema": "logs"}

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))


class EventTypeOrm(Base):
    __tablename__ = "event_type"
    __table_args__ = {"schema": "logs"}

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))


class LogOrm(Base):
    __tablename__ = "logs"
    __table_args__ = {"schema": "logs"}

    id: Mapped[int] = mapped_column(primary_key=True)
    datetime: Mapped[dt] = mapped_column(DateTime)

    space_type_id: Mapped[int] = mapped_column(ForeignKey("logs.space_type.id"))
    event_type_id: Mapped[int] = mapped_column(ForeignKey("logs.event_type.id"))

    user_id: Mapped[int]
    entity_id: Mapped[int]
