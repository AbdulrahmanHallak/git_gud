from datetime import date, datetime

from sqlmodel import SQLModel, Field, Relationship
from typing import Optional,List, TYPE_CHECKING
if TYPE_CHECKING:
    from src.app.models.Split import Split
    from src.app.models.User import User
    from src.app.models.PlanExercise import PlanExercise
    
    

class Plan(SQLModel, table=True):
    __tablename__ = "plans"

    id: int = Field(default_factory=int, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    split_id: int = Field(foreign_key="splits.id")

    start_date: date
    end_date: Optional[date] = None
    goal: Optional[str] = None
    status: str = Field(default="active")

    created_at: datetime = Field(default_factory=datetime.utcnow)

    user: "User" = Relationship(back_populates="plans")
    split: "Split" = Relationship(back_populates="plans")
    plan_exercises: List["PlanExercise"] = Relationship(back_populates="plan")
