import os
import ast
from serializers.formats import flatbuffer, protobuf
from utils.utils import ExecuteTerminalCommand
from events.base import Event


class FindEvents:
    def __init__(
            self, 
            events_dir,
            events_directory_name='events',
            ):
        self.events_dir=events_dir
        self.events_directory_name = events_directory_name
        
    def find_base_class_fields(self):
        fields_info = []
        for field_name, field_type in Event.__annotations__.items():
            default_value = None
            if hasattr(Event, field_name):
                default_value = getattr(Event, field_name).default

            fields_info.append({
                'name': field_name,
                'type': str(field_type).replace("<class '", '').replace("'>", '').strip(),
                'default_value': default_value,
        })
        return fields_info

    def find_file_events(self, file_path):
        events = list()
        base_event_fields = self.find_base_class_fields()
        with open(file_path, "r") as file:
            tree = ast.parse(file.read(), filename=file_path)
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.ClassDef)
                and any(base.id == "Event" for base in node.bases)
            ):
                try:
                    event_fields = list()
                    for field in node.body:
                        field_data = {"name": field.target.id,
                                      "type": field.annotation.id,
                                      "default_value": field.value.n if field.value else None}
                        event_fields.append(field_data)
                    events.extend(base_event_fields)
                    events.append({'name': node.name, 'fields': event_fields})
                except Exception as e:
                    events.append({'name': node.name, 'fields': base_event_fields})
        return events

    def get_events(self):
        events_directory = os.path.join(self.events_dir, self.events_directory_name)
        events = list()
        for file_name in os.listdir(events_directory):
            if file_name.endswith(".py") and file_name != __file__:
                file_path = os.path.join(events_directory, file_name)
                events.extend(self.find_file_events(file_path))
        return events
    

class MakeEventSchema: # TODO make serializer . directory clean
    def __init__(
            self, 
            events,
            events_dir
            ):
        self.events_dir=events_dir
        self.make_schema(events)

    def make_schema(self, events):
        fb = flatbuffer.Schema(events)
        pb = protobuf.Schema(events)
        fb_absolute_path = os.path.abspath(os.path.join("serializers", ".flatbuffer", fb.file_name))
        pb_absolute_path = os.path.abspath(os.path.join("serializers", ".protobuf"))
        ExecuteTerminalCommand(f"flatc --python {fb_absolute_path}", path=os.path.abspath(os.path.join("serializers", ".flatbuffer")))
        ExecuteTerminalCommand(f"protoc -I {pb_absolute_path} {pb.file_name} --python_out=.", path=os.path.abspath(os.path.join(self.events_dir, "serializers/.protobuf")))

