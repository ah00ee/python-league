import requests


class UrlHandler:
    def __init__(self, api_key) -> None:
        self._api_key = api_key
        self._request_headers = {
            "X-Riot-Token": self.api_key
        }
    
    @property
    def api_key(self):
        """
        Get: api_key
        """
        return self._api_key
 
    def request(self, url, params=None):
        res = requests.get(
            url=url,
            headers=self._request_headers,
            params=params
        )
        res.raise_for_status()

        return res.json()
