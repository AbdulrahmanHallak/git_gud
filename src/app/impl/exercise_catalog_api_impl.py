from sqlmodel import select
from src.app.db import get_session
from src.app.models.Exercise import Exercise
from src.app.models.MusclePartSplitDay import MusclePartSplitDay
from src.app.models.MusclePart import MusclePart
from src.app.models.SplitDay import SplitDay

from src.app.schema.exercise_list import ExerciseList, ExerciseListItem
from src.app.schema.exercise_detail import ExerciseDetail
from src.app.schema.error import Error

from typing import Optional, List

class ExerciseCatalogApiImpl:
    """Concrete implementation of BaseExerciseCatalogApi"""

    async def api_v1_exercises_get(
        self,
        type: Optional[str] = None,
        target_muscle: List[str] = None,
        equipment: Optional[str] = None,
        difficulty: Optional[str] = None,
        page: int = 1,
        limit: int = 20,
        search: Optional[str] = None,
    ) -> ExerciseList:
        async with get_session() as session:
            query = select(Exercise)

            if type:
                query = query.where(Exercise.type == type)
            if equipment:
                query = query.where(Exercise.equipment == equipment)
            if difficulty:
                query = query.where(Exercise.difficulty == difficulty)
            if search:
                query = query.where(Exercise.name.ilike(f"%{search}%"))

            # Pagination
            offset = (page - 1) * limit
            results = (await session.exec(query.offset(offset).limit(limit))).all()

            items: List[ExerciseListItem] = [
                ExerciseListItem(
                    id=str(e.id),
                    name=e.name,
                    type=e.type,
                    equipment=e.equipment,
                    difficulty=e.difficulty
                )
                for e in results
            ]

            return ExerciseList(total=len(items), items=items)

    async def api_v1_exercises_exercise_id_get(self, exerciseId: str) -> ExerciseDetail:
        async with get_session() as session:
            query = select(Exercise).where(Exercise.id == int(exerciseId))
            exercise = (await session.exec(query)).first()
            if not exercise:
                raise Exception("Exercise not found")

            # Build detail, you can extend with related muscles etc.
            return ExerciseDetail(
                id=str(exercise.id),
                name=exercise.name,
                type=exercise.type,
                equipment=exercise.equipment,
                difficulty=exercise.difficulty,
                instructions=exercise.instructions
            )

    async def api_v1_admin_exercises_exercise_id_delete(self, exerciseId: str) -> None:
        async with get_session() as session:
            query = select(Exercise).where(Exercise.id == int(exerciseId))
            exercise = (await session.exec(query)).first()
            if not exercise:
                raise Exception("Exercise not found")

            await session.delete(exercise)
            await session.commit()
            return None
