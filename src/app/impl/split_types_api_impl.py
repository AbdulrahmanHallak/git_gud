from sqlmodel import select
from src.app.db import get_session
from src.app.models.Split import Split
from src.app.models.SplitDay import SplitDay
from src.app.schema.api_v1_splits_get200_response import ApiV1SplitsGet200Response, SplitListItem
from src.app.schema.split_detail import SplitDetail, SplitDayItem
from src.app.schema.error import Error
from typing import List, Optional


class SplitTypesApiImpl:
    """Concrete implementation of BaseSplitTypesApi"""

    async def api_v1_splits_get(self) -> ApiV1SplitsGet200Response:
        async with get_session() as session:
            splits: List[Split] = (await session.exec(select(Split))).all()

            items = [
                SplitListItem(
                    id=str(split.id),
                    name=split.name,
                    description=split.description
                )
                for split in splits
            ]

            return ApiV1SplitsGet200Response(total=len(items), items=items)

    async def api_v1_splits_split_id_get(self, splitId: str) -> SplitDetail:
        async with get_session() as session:
            split: Optional[Split] = (await session.exec(select(Split).where(Split.id == int(splitId)))).first()
            if not split:
                raise Exception("Split not found")

            # Fetch related SplitDays
            split_days: List[SplitDay] = (await session.exec(select(SplitDay).where(SplitDay.split_id == split.id))).all()

            day_items = [
                SplitDayItem(
                    id=str(day.id),
                    name=day.name,
                    description=day.description,
                    order=day.order
                )
                for day in split_days
            ]

            return SplitDetail(
                id=str(split.id),
                name=split.name,
                description=split.description,
                days=day_items
            )
