import os
import subprocess
import sys
import textwrap
from setuptools import setup, find_packages
from subprocess import call
from utils.utils import RED, GREEN, RESET, ExecuteTerminalCommand

assistant_content = """import argparse
import ast
import os
from utils.utils import ExecuteTerminalCommand


class MakeEventSchema:
    def __init__(self) -> None:
        self.setup()

    def find_event_base_classes(self, file_path):
        with open(file_path, "r") as file:
            tree = ast.parse(file.read(), filename=file_path)

        event_base_classes = []
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.ClassDef)
                and any(base.id == "Event" for base in node.bases)
            ):
                event_base_classes.append(node.name)

        return event_base_classes
    
    def setup(self):
        ExecuteTerminalCommand('cd events')
        current_dir = os.path.dirname(os.path.abspath(__file__))
        for file_name in os.listdir(current_dir):
            if file_name.endswith(".py") and file_name != __file__:
                file_path = os.path.join(current_dir, file_name)
                event_base_classes = self.find_event_base_classes(file_path)
                if event_base_classes:
                    print(f"File: {file_name}, Classes: {event_base_classes}")


def main():
    parser = argparse.ArgumentParser(description="Events Library Assistant")
    parser.add_argument("command", choices=["startproject", "makeschema"], help="Command to execute")

    args = parser.parse_args()

    if args.command == "makeschema":
        MakeEventSchema()

if __name__ == "__main__":
    main()"""


class StartProject: 
    def __init__(self,) -> None:
        self.start_project()
        self.create_assistant()

    def create_assistant(self):
        ExecuteTerminalCommand(f"echo {assistant_content} >> assistant.py")

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
setup(
    name='events',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pika',
        'flatbuffers',
    ],
    entry_points={
        'console_scripts': [
            'startproject = events.module:StartProject',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='django-event-driven library',
    author='Gemmara',
    author_email='gemmarakaviani@gmail.com',
    description='A library for building event-driven systems',
    license='MIT',
    python_requires='>=3.8',
)
