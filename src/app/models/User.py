from datetime import date, datetime
from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from src.app.models.Biometric import Biometric
    from src.app.models.Plan import Plan


class User(SQLModel, table=True):
    __tablename__ = "users"  # type: ignore

    id: int = Field(default_factory=int, primary_key=True)
    email: str = Field(index=True, unique=True, nullable=False)
    password_hash: str

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    gender: Optional[str] = None
    date_of_birth: Optional[date] = None
    height_cm: Optional[float] = None
    experience_level: Optional[str] = None

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    biometrics: List["Biometric"] = Relationship(back_populates="user")
    plans: List["Plan"] = Relationship(back_populates="user")
