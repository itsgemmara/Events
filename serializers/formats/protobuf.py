class Schema:
    def __init__(
            self,
            events_data,
            message_pattern=["\nmessage {event_name} {{\n", "  {field_type} {field_name} = {field_number};\n"],
            files_start_pattern='syntax = "proto3";\n',
            files_end_pattern='',
            file_name='event.proto',
            output_directory='serializers/.protobuf',
    ) -> None:
        self.format_name = 'protobuf'
        self.protobuf_type = {
            'int': 'int32',
            'float': 'float',
            'bool': 'bool',
            'str': 'string',
            'bytes': 'bytes',
            'datetime.datetime': 'string'

        }
        self.events_data = events_data
        self.message_pattern = message_pattern
        self.files_start_pattern = files_start_pattern
        self.files_end_pattern = files_end_pattern
        self.file_name = file_name
        self.output_directory = output_directory
        self.setup()

    def setup(self):
        messages_list = [self.create_message(event) for event in self.events_data]
        self.create_file(messages_list)

    def create_message(self, event):
        message_start_pattern, field_pattern = self.message_pattern
        message_text = message_start_pattern.format(event_name=event['name'])
        for i, field in enumerate(event['fields'], start=1):
            message_text += field_pattern.format(
                field_type=self.protobuf_type[field['type']],
                field_name=field['name'],
                field_number=i,
            )
        message_text += '}\n'
        return message_text

    def create_file(self, messages_list):
        content = [self.files_start_pattern]
        content.extend(messages_list)
        content.append(self.files_end_pattern)

        file_path = f'{self.output_directory}/{self.file_name}'
        with open(file_path, 'w') as file:
            file.writelines(content)
