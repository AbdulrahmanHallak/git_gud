
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional ,TYPE_CHECKING
if TYPE_CHECKING:
    from src.app.models.Plan import Plan
    from src.app.models.SplitDay import SplitDay
    from src.app.models.Exercise import Exercise

class PlanExercise(SQLModel, table=True):
    __tablename__ = "plan_exercises"

    id: int = Field(default_factory=int, primary_key=True)
    plan_id: int = Field(foreign_key="plans.id")
    split_day_id: int = Field(foreign_key="split_days.id")
    exercise_id: int = Field(foreign_key="exercises.id")

    sets: int
    reps: str
    rest_seconds: Optional[int] = None
    tempo: Optional[str] = None
    order_index: int
    progression_rule: Optional[str] = None

    plan: "Plan" = Relationship(back_populates="plan_exercises")
    split_day: "SplitDay" = Relationship(back_populates="plan_exercises")
    exercise: "Exercise" = Relationship(back_populates="plan_exercises")
