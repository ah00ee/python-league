from .models import Summoner, Match
from .utils import UrlHandler


class LeagueAPI:

    def __init__(self, api_key="", platform="kr", region="asia"):   
        self.api_handler = UrlHandler(api_key=api_key)
        self.platform = platform
        self.region = region

    def get_summoner(self, summoner_name):
        return self._get_summoner(summoner_name=summoner_name)

    def _get_summoner(self, summoner_name):
        url = f'https://{self.platform}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}'
        res = self.api_handler.request(url=url)

        return Summoner(
                    self.api_handler,
                    platform=self.platform, 
                    region=self.region,
                    **res
                )

    def get_match(self, matchId):
        return self._get_match(matchId=matchId)

    def _get_match(self, matchId):
        url = f'https://{self.region}.api.riotgames.com/lol/match/v5/matches/{matchId}'
        res = self.api_handler.request(url=url)

        return Match(**res)


if __name__ == "__main__":
    lol = LeagueAPI(api_key="Your API Key")

    summoner = lol.get_summoner(summoner_name="summoner name")
    champion_mastery = summoner.get_champion_mastery() #champion mastery list of *summoner*