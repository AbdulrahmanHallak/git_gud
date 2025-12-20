from typing import ClassVar, Dict, List, Tuple 

from pydantic import StrictInt, StrictStr, field_validator
from typing import Any, Optional
from src.app.schema.error import Error
from src.app.schema.exercise_detail import ExerciseDetail
from src.app.schema.exercise_list import ExerciseList
from security_api import get_token_bearerAuth

class BaseExerciseCatalogApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseExerciseCatalogApi.subclasses = BaseExerciseCatalogApi.subclasses + (cls,)
    async def api_v1_exercises_get(
        self,
        type: Optional[StrictStr],
        target_muscle: Optional[StrictStr],
        equipment: Optional[StrictStr],
        difficulty: Optional[StrictStr],
        page: Optional[StrictInt],
        limit: Optional[StrictInt],
        search: Optional[StrictStr],
    ) -> ExerciseList:
        ...


    async def api_v1_exercises_exercise_id_get(
        self,
        exerciseId: StrictStr,
    ) -> ExerciseDetail:
        ...


    async def api_v1_admin_exercises_exercise_id_delete(
        self,
        exerciseId: StrictStr,
    ) -> None:
        ...
