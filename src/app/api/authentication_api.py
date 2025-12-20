# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.authentication_api_base import BaseAuthenticationApi
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
from typing import Any
from openapi_server.models.api_v1_auth_login_post_request import ApiV1AuthLoginPostRequest
from openapi_server.models.api_v1_auth_refresh_post_request import ApiV1AuthRefreshPostRequest
from openapi_server.models.api_v1_auth_signup_post_request import ApiV1AuthSignupPostRequest
from openapi_server.models.auth_response import AuthResponse
from openapi_server.models.error import Error
from openapi_server.models.token_response import TokenResponse


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/api/v1/auth/signup",
    responses={
        201: {"model": AuthResponse, "description": "User successfully registered"},
        400: {"model": Error, "description": "Invalid input"},
        409: {"model": Error, "description": "User already exists"},
    },
    tags=["Authentication"],
    summary="Register a new user",
    response_model_by_alias=True,
)
async def api_v1_auth_signup_post(
    api_v1_auth_signup_post_request: ApiV1AuthSignupPostRequest = Body(None, description=""),
) -> AuthResponse:
    if not BaseAuthenticationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAuthenticationApi.subclasses[0]().api_v1_auth_signup_post(api_v1_auth_signup_post_request)


@router.post(
    "/api/v1/auth/login",
    responses={
        200: {"model": AuthResponse, "description": "Successfully authenticated"},
        401: {"model": Error, "description": "Invalid credentials"},
    },
    tags=["Authentication"],
    summary="Authenticate a user",
    response_model_by_alias=True,
)
async def api_v1_auth_login_post(
    api_v1_auth_login_post_request: ApiV1AuthLoginPostRequest = Body(None, description=""),
) -> AuthResponse:
    if not BaseAuthenticationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAuthenticationApi.subclasses[0]().api_v1_auth_login_post(api_v1_auth_login_post_request)


@router.post(
    "/api/v1/auth/refresh",
    responses={
        200: {"model": TokenResponse, "description": "Token refreshed successfully"},
        401: {"model": Error, "description": "Invalid or expired refresh token"},
    },
    tags=["Authentication"],
    summary="Refresh access token",
    response_model_by_alias=True,
)
async def api_v1_auth_refresh_post(
    api_v1_auth_refresh_post_request: ApiV1AuthRefreshPostRequest = Body(None, description=""),
) -> TokenResponse:
    if not BaseAuthenticationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAuthenticationApi.subclasses[0]().api_v1_auth_refresh_post(api_v1_auth_refresh_post_request)


@router.post(
    "/api/v1/auth/logout",
    responses={
        204: {"description": "Successfully logged out"},
        400: {"model": Error, "description": "Invalid request"},
    },
    tags=["Authentication"],
    summary="Logout user and invalidate refresh token",
    response_model_by_alias=True,
)
async def api_v1_auth_logout_post(
    api_v1_auth_refresh_post_request: ApiV1AuthRefreshPostRequest = Body(None, description=""),
) -> None:
    if not BaseAuthenticationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAuthenticationApi.subclasses[0]().api_v1_auth_logout_post(api_v1_auth_refresh_post_request)
