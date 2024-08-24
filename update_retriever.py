import requests

class UpdateRetriever:
    def __init__(self, subscription_manager, config):
        self.subscription_manager = subscription_manager
        self.github_api_key = config['github_api_key']

    def fetch_updates(self):
        headers = {'Authorization': f'token {self.github_api_key}'}
        updates = {}
        for repo in self.subscription_manager.list_subscriptions():
            url = f'https://api.github.com/repos/{repo}/releases/latest'
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                latest_release = response.json()
                updates[repo] = {
                    'tag_name': latest_release['tag_name'],
                    'name': latest_release['name'],
                    'published_at': latest_release['published_at'],
                    'body': latest_release['body']
                }
            else:
                updates[repo] = 'No release information found'
        return updates

