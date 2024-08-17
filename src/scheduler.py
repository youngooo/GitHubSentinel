import schedule
import time
from src.subscription_manager import SubscriptionManager
from src.update_fetcher import UpdateFetcher
from src.notification_manager import NotificationManager
from src.report_generator import ReportGenerator

class Scheduler:
    def __init__(self, daily=False, weekly=False):
        self.subscription_manager = SubscriptionManager()
        self.update_fetcher = UpdateFetcher()
        self.notification_manager = NotificationManager()
        self.report_generator = ReportGenerator()
        self.daily = daily
        self.weekly = weekly

    def schedule_updates(self):
        if self.daily:
            schedule.every().day.at('08:00').do(self.run_tasks)
        elif self.weekly:
            schedule.every().monday.at('08:00').do(self.run_tasks)

    def run_tasks(self):
        subscriptions = self.subscription_manager.get_active_subscriptions()
        updates = self.update_fetcher.fetch_updates(subscriptions)
        reports = self.report_generator.generate_reports(updates)
        self.notification_manager.send_notifications(reports)

    def run(self):
        self.schedule_updates()
        while True:
            schedule.run_pending()
            time.sleep(1)
