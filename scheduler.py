import schedule
import time

def run_daily_updates():
    print("Running daily updates...")

def schedule_tasks():
    schedule.every().day.at("09:00").do(run_daily_updates)
    while True:
        schedule.run_pending()
        time.sleep(60)
