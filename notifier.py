class Notifier:
    def __init__(self, config):
        self.email = config['notification_email']

    def send_notification(self, message):
        print(f"Sending notification to {self.email}: {message}")
