import requests
from src.config import Config

class UpdateFetcher:
    def fetch_updates(self, subscriptions):
        headers = {'Authorization': f'token {Config.API_KEY}'}
        updates = []
        for repo in subscriptions:
            response = requests.get(repo, headers=headers)
            if response.status_code == 200:
                updates.append(response.json())
        return updates
