
from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.app.models.MusclePartSplitDay import MusclePartSplitDay


class SplitDay(SQLModel, table=True):
    __tablename__ = "split_days"

    id: int = Field(default_factory=int, primary_key=True)
    split_id: int = Field(foreign_key="splits.id")

    name: str
    day_order: int

    muscle_targets: list["MusclePartSplitDay"] = Relationship(
        back_populates="split_day"
    )
