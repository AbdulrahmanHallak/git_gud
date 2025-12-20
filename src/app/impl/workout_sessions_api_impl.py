from sqlmodel import select
from src.app.db import get_session
from src.app.models.PlanExercise import PlanExercise
from src.app.models.WorkoutLog import WorkoutLog
from src.app.schema.exercise_log import ExerciseLog
from fastapi import HTTPException
from datetime import datetime


class WorkoutSessionsApiImpl:
    """Concrete implementation of BaseWorkoutSessionsApi"""

    async def api_v1_users_user_id_plans_plan_id_exercises_exercise_id_patch(
        self,
        userId: int,
        planId: str,
        exerciseId: str,
        api_v1_users_user_id_plans_plan_id_exercises_exercise_id_patch_request
    ) -> ExerciseLog:
        async with get_session() as session:
            # Validate PlanExercise exists for this user, plan, and exercise
            query = select(PlanExercise).where(
                PlanExercise.plan_id == int(planId),
                PlanExercise.exercise_id == exerciseId
            )
            plan_exercise = (await session.exec(query)).first()
            if not plan_exercise:
                raise HTTPException(status_code=404, detail="Exercise not found in this plan")

            # Create new workout log entry
            log = WorkoutLog(
                user_id=userId,
                plan_exercise_id=plan_exercise.id,
                performed_at=datetime.utcnow(),
                sets=api_v1_users_user_id_plans_plan_id_exercises_exercise_id_patch_request.sets,
                reps=api_v1_users_user_id_plans_plan_id_exercises_exercise_id_patch_request.reps,
                weight_kg=api_v1_users_user_id_plans_plan_id_exercises_exercise_id_patch_request.weight_kg,
                note=api_v1_users_user_id_plans_plan_id_exercises_exercise_id_patch_request.note,
            )

            session.add(log)
            await session.commit()
            await session.refresh(log)

            return ExerciseLog(
                id=log.id,
                plan_exercise_id=log.plan_exercise_id,
                performed_at=log.performed_at,
                sets=log.sets,
                reps=log.reps,
                weight_kg=log.weight_kg,
                note=log.note
            )
