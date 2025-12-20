# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from typing import Any
from src.app.schema.api_v1_auth_login_post_request import ApiV1AuthLoginPostRequest
from src.app.schema.api_v1_auth_refresh_post_request import ApiV1AuthRefreshPostRequest
from src.app.schema.api_v1_auth_signup_post_request import ApiV1AuthSignupPostRequest
from src.app.schema.auth_response import AuthResponse
from src.app.schema.error import Error
from src.app.schema.token_response import TokenResponse


class BaseAuthenticationApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseAuthenticationApi.subclasses = BaseAuthenticationApi.subclasses + (cls,)
    async def api_v1_auth_signup_post(
        self,
        api_v1_auth_signup_post_request: ApiV1AuthSignupPostRequest,
    ) -> AuthResponse:
        ...


    async def api_v1_auth_login_post(
        self,
        api_v1_auth_login_post_request: ApiV1AuthLoginPostRequest,
    ) -> AuthResponse:
        ...


    async def api_v1_auth_refresh_post(
        self,
        api_v1_auth_refresh_post_request: ApiV1AuthRefreshPostRequest,
    ) -> TokenResponse:
        ...


    async def api_v1_auth_logout_post(
        self,
        api_v1_auth_refresh_post_request: ApiV1AuthRefreshPostRequest,
    ) -> None:
        ...
