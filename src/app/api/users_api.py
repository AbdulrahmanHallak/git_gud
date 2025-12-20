# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.users_api_base import BaseUsersApi
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
from pydantic import StrictInt
from openapi_server.models.api_v1_users_user_id_put_request import ApiV1UsersUserIdPutRequest
from openapi_server.models.error import Error
from openapi_server.models.user import User
from openapi_server.models.user_update import UserUpdate
from openapi_server.security_api import get_token_bearerAuth

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/v1/users/{userId}",
    responses={
        200: {"model": User, "description": "User profile retrieved successfully"},
        404: {"model": Error, "description": "User not found"},
    },
    tags=["Users"],
    summary="Get user profile",
    response_model_by_alias=True,
)
async def api_v1_users_user_id_get(
    userId: StrictInt = Path(..., description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> User:
    if not BaseUsersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUsersApi.subclasses[0]().api_v1_users_user_id_get(userId)


@router.put(
    "/api/v1/users/{userId}",
    responses={
        200: {"model": UserUpdate, "description": "User profile updated successfully"},
        400: {"model": Error, "description": "Invalid input"},
        404: {"model": Error, "description": "User not found"},
    },
    tags=["Users"],
    summary="Update user profile",
    response_model_by_alias=True,
)
async def api_v1_users_user_id_put(
    userId: StrictInt = Path(..., description=""),
    api_v1_users_user_id_put_request: ApiV1UsersUserIdPutRequest = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> UserUpdate:
    if not BaseUsersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUsersApi.subclasses[0]().api_v1_users_user_id_put(userId, api_v1_users_user_id_put_request)
