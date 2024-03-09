import shutil
from utils.utils import ExecuteTerminalCommand


def create_assistant():
    source_file = 'core/assistant.py'
    destination_file = 'PythonEvents/assistant.py'
    ExecuteTerminalCommand('ls')
    shutil.copyfile(source_file, destination_file)


def start_project():
    ExecuteTerminalCommand(
        """
        mkdir PythonEvents
        cd PythonEvents
        touch assistant.py
        mkdir events
        mkdir consumers
        mkdir handlers
        mkdir serializers
        touch assistant.py
        cd serializers
        mkdir formats
        cd formats 
        mkdir .protobuffers
        mkdir .flatbuffers
        cd .protobuffers
        touch tabels.proto
        cd ..
        cd .flatbuffers
        touch tabels.fbs
        cd ../../..
        """)