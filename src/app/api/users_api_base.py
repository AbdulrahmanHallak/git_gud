# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import StrictInt
from src.app.schema.api_v1_users_user_id_put_request import ApiV1UsersUserIdPutRequest
from src.app.schema.error import Error
from src.app.schema.user import User
from src.app.schema.user_update import UserUpdate
from security_api import get_token_bearerAuth

class BaseUsersApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseUsersApi.subclasses = BaseUsersApi.subclasses + (cls,)
    async def api_v1_users_user_id_get(
        self,
        userId: StrictInt,
    ) -> User:
        ...


    async def api_v1_users_user_id_put(
        self,
        userId: StrictInt,
        api_v1_users_user_id_put_request: ApiV1UsersUserIdPutRequest,
    ) -> UserUpdate:
        ...
