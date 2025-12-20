# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.workout_sessions_api_base import BaseWorkoutSessionsApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from pydantic import StrictInt, StrictStr
from openapi_server.models.api_v1_users_user_id_plans_plan_id_exercises_exercise_id_patch_request import ApiV1UsersUserIdPlansPlanIdExercisesExerciseIdPatchRequest
from openapi_server.models.error import Error
from openapi_server.models.exercise_log import ExerciseLog
from openapi_server.security_api import get_token_bearerAuth

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.patch(
    "/api/v1/users/{userId}/plans/{planId}/exercises/{exerciseId}",
    responses={
        200: {"model": ExerciseLog, "description": "Exercise logged successfully"},
        400: {"model": Error, "description": "Invalid input"},
        404: {"model": Error, "description": "Exercise not found"},
    },
    tags=["Workout Sessions"],
    summary="Log exercise sets",
    response_model_by_alias=True,
)
async def api_v1_users_user_id_plans_plan_id_exercises_exercise_id_patch(
    userId: StrictInt = Path(..., description=""),
    planId: StrictStr = Path(..., description=""),
    exerciseId: StrictStr = Path(..., description=""),
    api_v1_users_user_id_plans_plan_id_exercises_exercise_id_patch_request: ApiV1UsersUserIdPlansPlanIdExercisesExerciseIdPatchRequest = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> ExerciseLog:
    if not BaseWorkoutSessionsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWorkoutSessionsApi.subclasses[0]().api_v1_users_user_id_plans_plan_id_exercises_exercise_id_patch(userId, planId, exerciseId, api_v1_users_user_id_plans_plan_id_exercises_exercise_id_patch_request)
