# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from exercise_catalog_api_base import BaseExerciseCatalogApi
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

from src.app.schema.extra_models import TokenModel  # noqa: F401
from pydantic import StrictInt, StrictStr, field_validator
from typing import Any, Optional
from src.app.schema.error import Error
from src.app.schema.exercise_detail import ExerciseDetail
from src.app.schema.exercise_list import ExerciseList
from security_api import get_token_bearerAuth

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/v1/exercises",
    responses={
        200: {"model": ExerciseList, "description": "Exercises retrieved successfully"},
    },
    tags=["Exercise Catalog"],
    summary="Search and browse exercises",
    response_model_by_alias=True,
)
async def api_v1_exercises_get(
    type: Optional[StrictStr] = Query(None, description="", alias="type"),
    target_muscle: Optional[StrictStr] = Query(None, description="", alias="targetMuscle"),
    equipment: Optional[StrictStr] = Query(None, description="", alias="equipment"),
    difficulty: Optional[StrictStr] = Query(None, description="", alias="difficulty"),
    page: Optional[StrictInt] = Query(1, description="", alias="page"),
    limit: Optional[StrictInt] = Query(20, description="", alias="limit"),
    search: Optional[StrictStr] = Query(None, description="", alias="search"),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> ExerciseList:
    if not BaseExerciseCatalogApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseExerciseCatalogApi.subclasses[0]().api_v1_exercises_get(type, target_muscle, equipment, difficulty, page, limit, search)


@router.get(
    "/api/v1/exercises/{exerciseId}",
    responses={
        200: {"model": ExerciseDetail, "description": "Exercise details retrieved successfully"},
        404: {"model": Error, "description": "Exercise not found"},
    },
    tags=["Exercise Catalog"],
    summary="Get detailed exercise information",
    response_model_by_alias=True,
)
async def api_v1_exercises_exercise_id_get(
    exerciseId: StrictStr = Path(..., description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> ExerciseDetail:
    if not BaseExerciseCatalogApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseExerciseCatalogApi.subclasses[0]().api_v1_exercises_exercise_id_get(exerciseId)


@router.delete(
    "/api/v1/admin/exercises/{exerciseId}",
    responses={
        204: {"description": "Exercise deleted successfully"},
        403: {"model": Error, "description": "Forbidden - Admin access required"},
        404: {"model": Error, "description": "Exercise not found"},
    },
    tags=["Exercise Catalog"],
    summary="Delete an exercise (Admin only)",
    response_model_by_alias=True,
)
async def api_v1_admin_exercises_exercise_id_delete(
    exerciseId: StrictStr = Path(..., description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> None:
    if not BaseExerciseCatalogApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseExerciseCatalogApi.subclasses[0]().api_v1_admin_exercises_exercise_id_delete(exerciseId)
