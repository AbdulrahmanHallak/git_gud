# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date
from pydantic import StrictInt, StrictStr
from typing import Optional
from src.app.schema.error import Error
from src.app.schema.exercise_history import ExerciseHistory
from src.app.schema.exercise_progress import ExerciseProgress
from security_api import get_token_bearerAuth

class BaseExerciseHistoryApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseExerciseHistoryApi.subclasses = BaseExerciseHistoryApi.subclasses + (cls,)
    async def api_v1_users_user_id_exercises_exercise_id_history_get(
        self,
        userId: StrictInt,
        exerciseId: StrictStr,
        page: Optional[StrictInt],
        limit: Optional[StrictInt],
        start_date: Optional[date],
        end_date: Optional[date],
    ) -> ExerciseHistory:
        ...


    async def api_v1_users_user_id_exercises_exercise_id_progress_get(
        self,
        userId: StrictInt,
        exerciseId: StrictStr,
    ) -> ExerciseProgress:
        ...
