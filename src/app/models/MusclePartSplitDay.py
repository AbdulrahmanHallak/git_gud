from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from src.app.models.Split import SplitDay
    from src.app.models.Muscle import MuscleMusclePart
class MusclePartSplitDay(SQLModel, table=True):
    __tablename__ = "muscle_part_split_day"

    id: int = Field(default_factory=int, primary_key=True)

    split_day_id: int = Field(
        foreign_key="split_days.id",
        nullable=False
    )

    muscle_muscle_part_id: int = Field(
        foreign_key="muscle_muscle_parts.id",
        nullable=False
    )

    weekly_frequency: int = Field(nullable=False)
    priority: int = Field(nullable=False)

    split_day: "SplitDay" = Relationship(back_populates="muscle_targets")
    muscle_muscle_part: "MuscleMusclePart" = Relationship(back_populates="split_days")
