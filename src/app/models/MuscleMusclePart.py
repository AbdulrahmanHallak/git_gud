from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.app.models.MusclePartSplitDay import MusclePartSplitDay
    from src.app.models.ExerciseMuscleTarget import ExerciseMuscleTarget
    from src.app.models.Muscle import Muscle
    from src.app.models.MusclePart import MusclePart


class MuscleMusclePart(SQLModel, table=True):
    __tablename__ = "muscle_muscle_parts"  # type: ignore
    id: int = Field(default_factory=int, primary_key=True)
    muscle_id: int = Field(foreign_key="muscles.id")
    muscle_part_id: int = Field(foreign_key="muscle_parts.id")
    display_name: str

    muscle: "Muscle" = Relationship(back_populates="muscle_parts")
    muscle_part: "MusclePart" = Relationship(back_populates="muscle_muscle_parts")

    split_days: list["MusclePartSplitDay"] = Relationship(
        back_populates="muscle_muscle_part"
    )
    exercise_targets: list["ExerciseMuscleTarget"] = Relationship(
        back_populates="muscle_muscle_part"
    )
