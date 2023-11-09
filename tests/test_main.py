from league.models import *


class TestLeagueAPI:
    def test_get_summoner(self, api):
        summoner = api.get_summoner(summoner_name="summoner_name")
        return isinstance(summoner, Summoner)

    def test_get_match(self, api):
        match = api.get_match(matchId="matchId")
        return isinstance(match, Match)

    def test_get_champion_by_id(self, api):
        return isinstance(api.get_champion_by_id(championId="championId"), Champion)

    def test_get_champion_by_name(self, api):
        return isinstance(api.get_champion_by_name(championName="championName"), Champion)