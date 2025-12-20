# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from workout_plans_api_base import BaseWorkoutPlansApi
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
from src.app.schema.api_v1_users_user_id_plans_post_request import ApiV1UsersUserIdPlansPostRequest
from src.app.schema.error import Error
from src.app.schema.plan_detail import PlanDetail
from src.app.schema.plan_summary import PlanSummary
from src.app.schema.plans_list import PlansList
from security_api import get_token_bearerAuth

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/v1/users/{userId}/plans",
    responses={
        200: {"model": PlansList, "description": "Workout plans retrieved successfully"},
        404: {"model": Error, "description": "User not found"},
    },
    tags=["Workout Plans"],
    summary="Get user&#39;s workout plans",
    response_model_by_alias=True,
)
async def api_v1_users_user_id_plans_get(
    userId: StrictInt = Path(..., description=""),
    status: Optional[StrictStr] = Query(None, description="", alias="status"),
    page: Optional[StrictInt] = Query(1, description="", alias="page"),
    limit: Optional[StrictInt] = Query(10, description="", alias="limit"),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> PlansList:
    if not BaseWorkoutPlansApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWorkoutPlansApi.subclasses[0]().api_v1_users_user_id_plans_get(userId, status, page, limit)


@router.post(
    "/api/v1/users/{userId}/plans",
    responses={
        201: {"model": PlanSummary, "description": "Workout plan created successfully"},
        400: {"model": Error, "description": "Invalid input"},
    },
    tags=["Workout Plans"],
    summary="Create a new workout plan",
    response_model_by_alias=True,
)
async def api_v1_users_user_id_plans_post(
    userId: StrictInt = Path(..., description=""),
    api_v1_users_user_id_plans_post_request: ApiV1UsersUserIdPlansPostRequest = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> PlanSummary:
    if not BaseWorkoutPlansApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWorkoutPlansApi.subclasses[0]().api_v1_users_user_id_plans_post(userId, api_v1_users_user_id_plans_post_request)


@router.get(
    "/api/v1/users/{userId}/plans/{planId}",
    responses={
        200: {"model": PlanDetail, "description": "Workout plan retrieved successfully"},
        404: {"model": Error, "description": "Plan not found"},
    },
    tags=["Workout Plans"],
    summary="Get detailed workout plan",
    response_model_by_alias=True,
)
async def api_v1_users_user_id_plans_plan_id_get(
    userId: StrictInt = Path(..., description=""),
    planId: StrictStr = Path(..., description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> PlanDetail:
    if not BaseWorkoutPlansApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWorkoutPlansApi.subclasses[0]().api_v1_users_user_id_plans_plan_id_get(userId, planId)


@router.delete(
    "/api/v1/users/{userId}/plans/{planId}",
    responses={
        204: {"description": "Plan deleted successfully"},
        404: {"model": Error, "description": "Plan not found"},
    },
    tags=["Workout Plans"],
    summary="Delete a workout plan",
    response_model_by_alias=True,
)
async def api_v1_users_user_id_plans_plan_id_delete(
    userId: StrictInt = Path(..., description=""),
    planId: StrictStr = Path(..., description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> None:
    if not BaseWorkoutPlansApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWorkoutPlansApi.subclasses[0]().api_v1_users_user_id_plans_plan_id_delete(userId, planId)
