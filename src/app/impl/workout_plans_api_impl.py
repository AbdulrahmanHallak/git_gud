from sqlmodel import select
from src.app.db import get_session
from src.app.models.Plan import Plan
from src.app.models.PlanExercise import PlanExercise
from src.app.models.Split import Split
from src.app.models.User import User
from src.app.models.Biometric import Biometric

from src.app.schema.plans_list import PlansList, PlanListItem
from src.app.schema.plan_summary import PlanSummary
from src.app.schema.plan_detail import PlanDetail, PlanExerciseItem
from fastapi import HTTPException
from typing import Optional, List
from datetime import date


class WorkoutPlansApiImpl:
    """Concrete implementation of BaseWorkoutPlansApi"""

    async def api_v1_users_user_id_plans_get(
        self,
        userId: int,
        status: Optional[str] = None,
        page: int = 1,
        limit: int = 10,
    ) -> PlansList:
        async with get_session() as session:
            # Validate user exists
            user = (await session.exec(select(User).where(User.id == userId))).first()
            if not user:
                raise HTTPException(status_code=404, detail="User not found")

            query = select(Plan).where(Plan.user_id == userId)
            if status:
                query = query.where(Plan.status == status)

            offset = (page - 1) * limit
            plans: List[Plan] = (await session.exec(query.offset(offset).limit(limit))).all()

            items = [
                PlanListItem(
                    id=str(plan.id),
                    split_id=plan.split_id,
                    start_date=plan.start_date,
                    end_date=plan.end_date,
                    status=plan.status,
                    goal=plan.goal
                )
                for plan in plans
            ]

            return PlansList(total=len(items), items=items)

    async def api_v1_users_user_id_plans_post(
        self,
        userId: int,
        api_v1_users_user_id_plans_post_request
    ) -> PlanSummary:
        async with get_session() as session:
            # Validate user exists
            user = (await session.exec(select(User).where(User.id == userId))).first()
            if not user:
                raise HTTPException(status_code=404, detail="User not found")

            # Create new plan
            plan = Plan(
                user_id=userId,
                split_id=api_v1_users_user_id_plans_post_request.split_id,
                start_date=api_v1_users_user_id_plans_post_request.start_date,
                end_date=api_v1_users_user_id_plans_post_request.end_date,
                goal=api_v1_users_user_id_plans_post_request.goal,
                status="active"
            )

            session.add(plan)
            await session.commit()
            await session.refresh(plan)

            return PlanSummary(
                id=plan.id,
                split_id=plan.split_id,
                start_date=plan.start_date,
                end_date=plan.end_date,
                status=plan.status,
                goal=plan.goal
            )

    async def api_v1_users_user_id_plans_plan_id_get(
        self,
        userId: int,
        planId: str
    ) -> PlanDetail:
        async with get_session() as session:
            plan: Plan = (await session.exec(select(Plan).where(Plan.id == int(planId), Plan.user_id == userId))).first()
            if not plan:
                raise HTTPException(status_code=404, detail="Plan not found")

            # Include related exercises
            exercises: List[PlanExercise] = (await session.exec(
                select(PlanExercise).where(PlanExercise.plan_id == plan.id)
            )).all()

            exercise_items = [
                PlanExerciseItem(
                    id=pe.id,
                    exercise_id=pe.exercise_id,
                    sets=pe.sets,
                    reps=pe.reps,
                    weight_kg=pe.weight_kg,
                    note=pe.note
                )
                for pe in exercises
            ]

            return PlanDetail(
                id=plan.id,
                user_id=plan.user_id,
                split_id=plan.split_id,
                start_date=plan.start_date,
                end_date=plan.end_date,
                status=plan.status,
                goal=plan.goal,
                exercises=exercise_items
            )

    async def api_v1_users_user_id_plans_plan_id_delete(
        self,
        userId: int,
        planId: str
    ) -> None:
        async with get_session() as session:
            plan: Plan = (await session.exec(select(Plan).where(Plan.id == int(planId), Plan.user_id == userId))).first()
            if not plan:
                raise HTTPException(status_code=404, detail="Plan not found")

            await session.delete(plan)
            await session.commit()
            return None
