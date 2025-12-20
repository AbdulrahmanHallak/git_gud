# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.split_types_api_base import BaseSplitTypesApi
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
from pydantic import StrictStr
from openapi_server.models.api_v1_splits_get200_response import ApiV1SplitsGet200Response
from openapi_server.models.error import Error
from openapi_server.models.split_detail import SplitDetail
from openapi_server.security_api import get_token_bearerAuth

router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/api/v1/splits",
    responses={
        200: {"model": ApiV1SplitsGet200Response, "description": "Split types retrieved successfully"},
    },
    tags=["Split Types"],
    summary="Get all workout split types",
    response_model_by_alias=True,
)
async def api_v1_splits_get(
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> ApiV1SplitsGet200Response:
    if not BaseSplitTypesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSplitTypesApi.subclasses[0]().api_v1_splits_get()


@router.get(
    "/api/v1/splits/{splitId}",
    responses={
        200: {"model": SplitDetail, "description": "Split details retrieved successfully"},
        404: {"model": Error, "description": "Split not found"},
    },
    tags=["Split Types"],
    summary="Get detailed split type information",
    response_model_by_alias=True,
)
async def api_v1_splits_split_id_get(
    splitId: StrictStr = Path(..., description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> SplitDetail:
    if not BaseSplitTypesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSplitTypesApi.subclasses[0]().api_v1_splits_split_id_get(splitId)
