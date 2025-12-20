# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import StrictInt, StrictStr
from openapi_server.models.api_v1_users_user_id_plans_plan_id_exercises_exercise_id_patch_request import ApiV1UsersUserIdPlansPlanIdExercisesExerciseIdPatchRequest
from openapi_server.models.error import Error
from openapi_server.models.exercise_log import ExerciseLog
from openapi_server.security_api import get_token_bearerAuth

class BaseWorkoutSessionsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseWorkoutSessionsApi.subclasses = BaseWorkoutSessionsApi.subclasses + (cls,)
    async def api_v1_users_user_id_plans_plan_id_exercises_exercise_id_patch(
        self,
        userId: StrictInt,
        planId: StrictStr,
        exerciseId: StrictStr,
        api_v1_users_user_id_plans_plan_id_exercises_exercise_id_patch_request: ApiV1UsersUserIdPlansPlanIdExercisesExerciseIdPatchRequest,
    ) -> ExerciseLog:
        ...
