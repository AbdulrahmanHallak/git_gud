from datetime import datetime

from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from src.app.models.User import User
    from src.app.models.Plan import Plan


class Biometric(SQLModel, table=True):
    __tablename__ = "biometrics"  # type: ignore

    id: int = Field(primary_key=True)

    user_id: int = Field(foreign_key="users.id", nullable=False)
    plan_id: int = Field(foreign_key="plans.id", nullable=False)

    weight_kg: Optional[float] = None
    body_fat_pct: Optional[float] = None
    muscle_mass_kg: Optional[float] = None
    bmi: Optional[float] = None

    recorded_at: datetime = Field(default_factory=datetime.utcnow)

    user: "User" = Relationship(back_populates="biometrics")
    plan: "Plan" = Relationship(back_populates="biometrics")
