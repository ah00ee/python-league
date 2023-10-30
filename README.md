# python-league
Python-league helps you to use League of Legends API.

## Installation
```
pip install python-league --upgrade
```

## How to use
```python
from league import LeagueAPI

lol = LeagueAPI(api_key="Your API KEY")

# 소환사 정보 가져오기
summoner = lol.get_summonerDto(summoner_name="summoner_name")

# 최근 매치 불러오기
matchIds = lol.get_recent_matchId(summoner_name="summoner_name")

# 매치 정보 불러오기
match = lol.get_matchDto(matchId="matchId")
```
