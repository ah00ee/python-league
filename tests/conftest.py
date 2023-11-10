import pytest

from league import LeagueAPI


@pytest.fixture()
def api():
    api = LeagueAPI(
                api_key="Your API KEY",
                platform="platform",
                region="region"
    )
    return api

@pytest.fixture()
def summoner(api):
    return api.get_summoner("Colleen")