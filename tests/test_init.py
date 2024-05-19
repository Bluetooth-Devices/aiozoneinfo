import pytest
import zoneinfo

from aiozoneinfo import async_get_time_zone


@pytest.mark.asyncio
async def test_async_get_time_zone():
    """Getting cached timezone."""
    zone_info = await async_get_time_zone("UTC")
    assert isinstance(zone_info, zoneinfo.ZoneInfo)
