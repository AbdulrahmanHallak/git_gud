
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List , TYPE_CHECKING
if TYPE_CHECKING:
    from src.app.models.Plan import Plan
    from src.app.models.SplitDay import SplitDay


class Split(SQLModel, table=True):
    __tablename__ = "splits"

    id: int = Field(default_factory=int, primary_key=True)
    name: str = Field(unique=True, nullable=False)
    description: Optional[str] = None
    days_per_week: int

    split_days: List["SplitDay"] = Relationship(back_populates="split")
    plans: List["Plan"] = Relationship(back_populates="split")
