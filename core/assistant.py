import argparse
import os
from events.utils import MakeEventSchema, FindEvents
from handlers.utils import MakeHandler


def main():
    parser = argparse.ArgumentParser(description="Events Library Assistant")
    parser.add_argument("command", choices=["makeschema"], help="Command to execute")
    args = parser.parse_args()
    if args.command == "makeschema":        
        os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        events_dir=os.getcwd()
        events = FindEvents(events_dir).get_events()
        MakeHandler(events)

if __name__ == "__main__":
    main()