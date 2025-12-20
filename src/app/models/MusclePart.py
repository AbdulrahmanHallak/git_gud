from sqlmodel import SQLModel, Field, Relationship
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from src.app.models.MuscleMusclePart import MuscleMusclePart
    
class MusclePart(SQLModel, table=True):
    __tablename__ = "muscle_parts"

    id: int = Field(default_factory=int, primary_key=True)
    name: str

    muscle_parts: List["MuscleMusclePart"] = Relationship(back_populates="muscle_part")
