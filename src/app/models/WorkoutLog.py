from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional 

class WorkoutLog(SQLModel, table=True):
    __tablename__ = "workout_logs"

    id: int = Field(default_factory=int, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    plan_id: int = Field(foreign_key="plans.id")
    plan_exercise_id: int = Field(foreign_key="plan_exercises.id")
    exercise_id: int = Field(foreign_key="exercises.id")

    performed_at: datetime = Field(default_factory=datetime.utcnow)
    set_number: int
    weight: float
    reps: int
    notes: Optional[str] = None
