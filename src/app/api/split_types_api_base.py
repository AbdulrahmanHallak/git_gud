# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import StrictStr
from src.app.schema.api_v1_splits_get200_response import ApiV1SplitsGet200Response
from src.app.schema.error import Error
from src.app.schema.split_detail import SplitDetail
from security_api import get_token_bearerAuth

class BaseSplitTypesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseSplitTypesApi.subclasses = BaseSplitTypesApi.subclasses + (cls,)
    async def api_v1_splits_get(
        self,
    ) -> ApiV1SplitsGet200Response:
        ...


    async def api_v1_splits_split_id_get(
        self,
        splitId: StrictStr,
    ) -> SplitDetail:
        ...
