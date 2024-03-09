import os
import subprocess
import textwrap
from subprocess import call

BLUE = "\033[94m"
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"


def _print(text, color_code):
    print(f"{color_code}{text}{RESET}")


class ExecuteTerminalCommand:
    def __init__(self, command, path=os.getcwd()) -> None:
        self.execute_command(command, path)
    def add_tab_in_lines(self, output):
        wrapped_output = textwrap.indent(textwrap.fill(output, width=80), "   ")
        return f"{wrapped_output}"

    def execute_command(self, command, path):
        os.chdir(path)
        try:
            
            result = subprocess.run(
                command,
                shell=True,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=path
            )
            _print(self.add_tab_in_lines(result.stdout), GREEN)
        except subprocess.CalledProcessError as e:
            _print(self.add_tab_in_lines(e.stderr), RED)


def convert_to_class_name(input_str):
    words = [word.capitalize() for word in input_str.split('_')]
    word = ''.join(words)
    return word if '_' in input_str else input_str[0].upper() + input_str[1:] 


def remove_trailing_newlines(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    modified_content = content.rstrip('\n')
    with open(file_path, 'w') as file:
        file.write(modified_content)
