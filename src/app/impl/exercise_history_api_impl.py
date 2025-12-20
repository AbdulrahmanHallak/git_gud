from sqlmodel import select
from src.app.db import get_session
from src.app.models.PlanExercise import PlanExercise
from src.app.models.WorkoutLog import WorkoutLog
from src.app.models.Exercise import Exercise
from src.app.models.User import User

from src.app.schema.exercise_history import ExerciseHistory, ExerciseHistoryItem
from src.app.schema.exercise_progress import ExerciseProgress
from src.app.schema.error import Error

from typing import List, Optional
from datetime import date


class ExerciseHistoryApiImpl:
    """Concrete implementation of BaseExerciseHistoryApi"""

    async def api_v1_users_user_id_exercises_exercise_id_history_get(
        self,
        userId: int,
        exerciseId: str,
        page: int = 1,
        limit: int = 10,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
    ) -> ExerciseHistory:
        async with get_session() as session:
            query = select(WorkoutLog).where(
                WorkoutLog.user_id == userId,
                WorkoutLog.exercise_id == int(exerciseId),
            )

            if start_date:
                query = query.where(WorkoutLog.performed_at >= start_date)
            if end_date:
                query = query.where(WorkoutLog.performed_at <= end_date)

            offset = (page - 1) * limit
            logs: List[WorkoutLog] = (await session.exec(query.offset(offset).limit(limit))).all()

            items = [
                ExerciseHistoryItem(
                    id=log.id,
                    performed_at=log.performed_at,
                    sets=log.sets,
                    reps=log.reps,
                    weight_kg=log.weight_kg,
                )
                for log in logs
            ]

            return ExerciseHistory(total=len(items), items=items)

    async def api_v1_users_user_id_exercises_exercise_id_progress_get(
        self,
        userId: int,
        exerciseId: str,
    ) -> ExerciseProgress:
        async with get_session() as session:
            query = select(WorkoutLog).where(
                WorkoutLog.user_id == userId,
                WorkoutLog.exercise_id == int(exerciseId),
            )

            logs: List[WorkoutLog] = (await session.exec(query)).all()
            if not logs:
                raise Exception("Exercise not found")

            # Example metrics
            total_weight = sum(log.reps * log.weight_kg for log in logs if log.weight_kg and log.reps)
            max_weight = max((log.weight_kg for log in logs if log.weight_kg), default=0)
            total_reps = sum(log.reps for log in logs if log.reps)

            return ExerciseProgress(
                total_weight_lifted=total_weight,
                max_weight=max_weight,
                total_reps=total_reps,
                session_count=len(logs),
            )
