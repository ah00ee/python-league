import pytest

from league import LeagueAPI


@pytest.fixture()
def api():
    api = LeagueAPI(
                api_key="api_key",
                platform="platform",
                region="region"
    )
    return api
