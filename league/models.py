

class Summoner:
    def __init__(self, api_handler, **kwargs):
        self.api_handler = api_handler
        self.__dict__.update(kwargs)

    def get_recent_matchId(self, 
                    startTime=None,
                    endTime=None,
                    queue=None,
                    type=None,
                    start=0,
                    count=20
                ):
        """Get a list of match ids by puuid

        startTime: long         #Epoch timestamp in seconds. (>06-16-2021)
        endTime: long           #Epoch timestamp in seconds.
        queue: int              #
        type: string            #
        start: int              #Defaults to 0. Start index.
        count: int              #Defaults to 20. (valid: 0 to 100)
        """    
        url = f'https://{self.region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{self.puuid}/ids'

        return self.api_handler.request(url=url,
                        params={
                            "startTime": startTime,
                            "endTime": endTime,
                            "queue": queue,
                            "type": type,
                            "start": start,
                            "count": count
                        })

    def get_champion_mastery(self):
        """Get all champion mastery entries sorted by number of champion points descending
        """
        url = f'https://{self.platform}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{self.puuid}'
        res = self.api_handler.request(url=url)

        return [ChampionMastery(**r) for r in res]


class Match:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class ChampionMastery:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

