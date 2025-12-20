# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import StrictInt, StrictStr, field_validator
from typing import Any, Optional
from openapi_server.models.api_v1_users_user_id_plans_post_request import ApiV1UsersUserIdPlansPostRequest
from openapi_server.models.error import Error
from openapi_server.models.plan_detail import PlanDetail
from openapi_server.models.plan_summary import PlanSummary
from openapi_server.models.plans_list import PlansList
from openapi_server.security_api import get_token_bearerAuth

class BaseWorkoutPlansApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseWorkoutPlansApi.subclasses = BaseWorkoutPlansApi.subclasses + (cls,)
    async def api_v1_users_user_id_plans_get(
        self,
        userId: StrictInt,
        status: Optional[StrictStr],
        page: Optional[StrictInt],
        limit: Optional[StrictInt],
    ) -> PlansList:
        ...


    async def api_v1_users_user_id_plans_post(
        self,
        userId: StrictInt,
        api_v1_users_user_id_plans_post_request: ApiV1UsersUserIdPlansPostRequest,
    ) -> PlanSummary:
        ...


    async def api_v1_users_user_id_plans_plan_id_get(
        self,
        userId: StrictInt,
        planId: StrictStr,
    ) -> PlanDetail:
        ...


    async def api_v1_users_user_id_plans_plan_id_delete(
        self,
        userId: StrictInt,
        planId: StrictStr,
    ) -> None:
        ...
