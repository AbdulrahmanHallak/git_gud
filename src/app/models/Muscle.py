
from sqlmodel import SQLModel, Field, Relationship
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from src.app.models.MuscleMusclePart import MuscleMusclePart
    
class Muscle(SQLModel, table=True):
    __tablename__ = "muscles"

    id: int = Field(default_factory=int, primary_key=True)
    name: str = Field(unique=True, nullable=False)

    muscle_parts: List["MuscleMusclePart"] = Relationship(back_populates="muscle")
