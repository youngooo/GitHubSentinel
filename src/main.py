import argparse
from src.scheduler import Scheduler

def parse_args():
    parser = argparse.ArgumentParser(description='Manage and track GitHub repository updates.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--daily', action='store_true', help='Run updates daily.')
    group.add_argument('--weekly', action='store_true', help='Run updates weekly.')
    return parser.parse_args()

def main():
    args = parse_args()
    scheduler = Scheduler(daily=args.daily, weekly=args.weekly)
    scheduler.run()

if __name__ == '__main__':
    main()
