from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from src.app.models.PlanExercise import PlanExercise
    from src.app.models.MusclePartSplitDay import MusclePartSplitDay
    from src.app.models.Split import Split


class SplitDay(SQLModel, table=True):
    __tablename__ = "split_days"  # type: ignore
    id: int = Field(default_factory=int, primary_key=True)
    split_id: int = Field(foreign_key="splits.id")
    name: str
    day_order: int

    split: "Split" = Relationship(back_populates="split_days")

    muscle_targets: List["MusclePartSplitDay"] = Relationship(
        back_populates="split_day"
    )
    plan_exercises: List["PlanExercise"] = Relationship(back_populates="split_day")
