from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from src.app.models.Exercise import Exercise
    from src.app.models.Muscle import MuscleMusclePart


class ExerciseMuscleTarget(SQLModel, table=True):
    __tablename__ = "exercise_muscle_targets"  # type: ignore

    id: int = Field(default_factory=int, primary_key=True)

    exercise_id: int = Field(foreign_key="exercises.id", nullable=False)

    muscle_muscle_part_id: int = Field(
        foreign_key="muscle_muscle_parts.id", nullable=False
    )

    activation_level: int = Field(nullable=False)

    exercise: "Exercise" = Relationship(back_populates="muscle_targets")
    muscle_muscle_part: "MuscleMusclePart" = Relationship(
        back_populates="exercise_targets"
    )
