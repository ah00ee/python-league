import requests


class LeagueAPI:
    api_key = ""

    def __init__(self, api_key="", platform="kr", region="asia"):   
        LeagueAPI.api_key = api_key

        self.platform = platform
        self.region = region

    def get_recent_matchId(self, 
                            summoner_name,
                            startTime=None,
                            endTime=None,
                            queue=None,
                            type=None,
                            start=0,
                            count=20
                        ):

        summoner = self.Summoner(summoner_name=summoner_name)
        puuid = summoner.summonerDTO['puuid']
        
        url = f'https://{self.region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids'
        res = requests.get(
                            url=url,
                            headers={
                                "X-Riot-Token":LeagueAPI.api_key
                            },
                            params={
                                "startTime":startTime,
                                "endTime":endTime,
                                "queue":queue,
                                "type":type,
                                "start":start,
                                "count":count
                            }
            )

        return res.json()


    class Summoner:

        def __init__(self, summoner_name=""):
            self.summonerDTO = self._get_summonerDTO(summoner_name)

        def _get_summonerDTO(self, summoner_name):
            url = f'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}/'
            res = requests.get(
                                url=url,
                                headers={
                                    "X-Riot-Token":LeagueAPI.api_key
                                }    
                )

            return res.json()

    
if __name__ == '__main__':
    lol = LeagueAPI(api_key="Your API KEY")
    match = lol.get_recent_matchId(summoner_name="")
    
    print(match)