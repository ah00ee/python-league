# python-league
Python-league는 Riot API를 사용하여 간편하게 리그 오브 레전드(롤) 데이터를 사용할 수 있도록 만든 python 라이브러리입니다.

## Installation
![Generic badge](https://img.shields.io/badge/pypi-v0.0.5-yellow.svg)
```
pip install python-league --upgrade
```

## Tutorial
Here's <a href="https://github.com/ah00ee/python-league/blob/main/tutorial.ipynb">tutorial</a> for your information.

## How to use
```python
from league import LeagueAPI

lol = LeagueAPI(api_key="Your API KEY")

summoner = lol.get_summoner(summoner_name="summoner name")
print(summoner.__dict__)
```
