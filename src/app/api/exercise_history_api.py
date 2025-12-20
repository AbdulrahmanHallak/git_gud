# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.exercise_history_api_base import BaseExerciseHistoryApi
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
from datetime import date
from pydantic import StrictInt, StrictStr
from typing import Optional
from openapi_server.models.error import Error
from openapi_server.models.exercise_history import ExerciseHistory
from openapi_server.models.exercise_progress import ExerciseProgress
from openapi_server.security_api import get_token_bearerAuth

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/v1/users/{userId}/exercises/{exerciseId}/history",
    responses={
        200: {"model": ExerciseHistory, "description": "Exercise history retrieved successfully"},
        404: {"model": Error, "description": "Exercise not found"},
    },
    tags=["Exercise History"],
    summary="Get exercise history",
    response_model_by_alias=True,
)
async def api_v1_users_user_id_exercises_exercise_id_history_get(
    userId: StrictInt = Path(..., description=""),
    exerciseId: StrictStr = Path(..., description=""),
    page: Optional[StrictInt] = Query(1, description="", alias="page"),
    limit: Optional[StrictInt] = Query(10, description="", alias="limit"),
    start_date: Optional[date] = Query(None, description="", alias="startDate"),
    end_date: Optional[date] = Query(None, description="", alias="endDate"),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> ExerciseHistory:
    if not BaseExerciseHistoryApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseExerciseHistoryApi.subclasses[0]().api_v1_users_user_id_exercises_exercise_id_history_get(userId, exerciseId, page, limit, start_date, end_date)


@router.get(
    "/api/v1/users/{userId}/exercises/{exerciseId}/progress",
    responses={
        200: {"model": ExerciseProgress, "description": "Exercise progress retrieved successfully"},
        404: {"model": Error, "description": "Exercise not found"},
    },
    tags=["Exercise History"],
    summary="Get exercise progress statistics",
    response_model_by_alias=True,
)
async def api_v1_users_user_id_exercises_exercise_id_progress_get(
    userId: StrictInt = Path(..., description=""),
    exerciseId: StrictStr = Path(..., description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> ExerciseProgress:
    if not BaseExerciseHistoryApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseExerciseHistoryApi.subclasses[0]().api_v1_users_user_id_exercises_exercise_id_progress_get(userId, exerciseId)
