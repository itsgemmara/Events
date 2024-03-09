import os 
import ast
from setting import ROOT_DIR
from utils.utils import convert_to_class_name, remove_trailing_newlines


class MakeHandler:
    def __init__(self, events_names_lists) -> None:
        self.all_events = events_names_lists
        self.existing_handlers_event_name = self.extract_existing_handlers()
        self.new_events = [event for event in self.all_events if event['name'] not in self.existing_handlers_event_name]
        print(self.new_events)
        self.create_handler()

    def extract_existing_handlers(self):
        if ROOT_DIR:
            handler_file_path = os.path.join(ROOT_DIR, "handlers.py")
            with open(handler_file_path, "r") as handler_file:
                tree = ast.parse(handler_file.read())
                existing_handlers = list()
                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef):
                        for base in node.bases:
                            if isinstance(base, ast.Name) and base.id == 'Handler':
                                event_name = self.extract_event_name(node)
                                existing_handlers.append(event_name)
                return existing_handlers
            
    def extract_event_name(self, class_node):
        for item in class_node.body:
            if isinstance(item, ast.Assign):
                for target in item.targets:
                    if isinstance(target, ast.Name) and target.id == 'event_name':
                        return item.value.s
    
    def create_handler(self):
        if ROOT_DIR:
            handler_file_path = os.path.join(ROOT_DIR, "handlers.py")
            remove_trailing_newlines(handler_file_path)
            with open(handler_file_path, "r+") as handler_file:
                if not handler_file.read():
                    handler_file.write("from events.handlers.base import Handler\n")
                    handler_file.write('\n')
                for event in self.new_events:
                    name = convert_to_class_name(event['name'])
                    handler_file.write(f"\nclass {name}Handler(Handler):\n   #Define you'r handler logic for handeling {event['name']} here.\n   event_name='{event['name']}'\n   pass\n")
                    handler_file.write('\n')
