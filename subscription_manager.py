class SubscriptionManager:
    def __init__(self, config):
        self.subscriptions = set()

    def add_repo(self, repo_name):
        self.subscriptions.add(repo_name)

    def remove_repo(self, repo_name):
        self.subscriptions.discard(repo_name)

    def list_subscriptions(self):
        return list(self.subscriptions)
