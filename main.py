import json
from cmd import Cmd
from subscription_manager import SubscriptionManager
from update_retriever import UpdateRetriever
from notifier import Notifier
from report_generator import ReportGenerator
from scheduler import schedule_tasks
import threading

def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)

class SentinelCLI(Cmd):
    intro = 'Welcome to GitHub Sentinel. Type help or ? to list commands.\n'
    prompt = '(GitHub Sentinel) '

    def __init__(self, config):
        super().__init__()
        self.subscription_manager = SubscriptionManager(config)
        self.update_retriever = UpdateRetriever(self.subscription_manager, config)
        self.notifier = Notifier(config)
        self.report_generator = ReportGenerator(self.update_retriever)

    def do_add(self, arg):
        'Add a new repository to subscribe: add <repo_name>'
        self.subscription_manager.add_repo(arg)
        print(f"Added repository: {arg}")

    def do_remove(self, arg):
        'Remove a repository from subscription: remove <repo_name>'
        self.subscription_manager.remove_repo(arg)
        print(f"Removed repository: {arg}")

    def do_list(self, arg):
        'List all subscribed repositories'
        subscriptions = self.subscription_manager.list_subscriptions()
        for repo in subscriptions:
            print(repo)

    def do_update(self, arg):
        'Fetch updates for all subscribed repositories and print report'
        updates = self.update_retriever.fetch_updates()
        report = self.report_generator.generate_report()
        print(report)

    def do_exit(self, arg):
        'Exit the program'
        print("Exiting...")
        return True

if __name__ == "__main__":
    config = load_config()
    cli = SentinelCLI(config)
    # Start the scheduler in a separate thread
    threading.Thread(target=schedule_tasks, daemon=True).start()
    cli.cmdloop()  # This should be called here, not typed in manually
