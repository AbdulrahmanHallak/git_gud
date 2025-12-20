from sqlmodel import SQLModel, Field, Relationship
from typing import Optional,List, TYPE_CHECKING
if TYPE_CHECKING:
    from src.app.models.PlanExercise import PlanExercise
    from src.app.models.ExerciseMuscleTarget import ExerciseMuscleTarget
   
class Exercise(SQLModel, table=True):
    __tablename__ = "exercises"

    id: int = Field(default_factory=int, primary_key=True)
    name: str = Field(unique=True, nullable=False)
    equipment: Optional[str] = None
    difficulty: Optional[str] = None
    is_compound: bool = False
    video_url: Optional[str] = None
    photo_url: Optional[str] = None
    
    plan_exercises: List["PlanExercise"] = Relationship(back_populates="exercise")
    muscle_targets: list["ExerciseMuscleTarget"] = Relationship(
        back_populates="exercise"
    )