import pytest

try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo  # type: ignore[no-redef]

from aiozoneinfo import async_get_time_zone


@pytest.mark.asyncio
async def test_async_get_time_zone():
    """Getting cached timezone."""
    zone_info = await async_get_time_zone("America/Los_Angeles")
    assert isinstance(zone_info, zoneinfo.ZoneInfo)
    assert zone_info.key == "America/Los_Angeles"
