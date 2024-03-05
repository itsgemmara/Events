from utils.utils import RED, GREEN, RESET, ExecuteTerminalCommand
import subprocess
assistant_content = """
import argparse
import ast
import os
from utils.utils import ExecuteTerminalCommand


class MakeEventSchema:
    def __init__(self) -> None:
        self.setup()
        return event_base_classes
    

"""

class StartProject: 
    def __init__(self,) -> None:
        self.start_project()
        self.create_assistant()

    def create_assistant(self):
        c = ''
        for line in assistant_content.splitlines():
            print(line)
            c += (line)

        ExecuteTerminalCommand(f'''
        cd PythonEvents
        ls
        echo {c} >> assistant.py 
        ''')
        # with open("assistant.py", "w") as assistant_file:
        #     for line in assistant_content.splitlines():
        #         assistant_file.write(line)

    
    def start_project(self):
        ExecuteTerminalCommand(
            f"""
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
StartProject()