import sys

from cliff.app import App
from cliff.commandmanager import CommandManager


class DemoApp(App):
    def __init__(self):
        super(DemoApp, self).__init__(
            description='cliff demo app',
            version='0.1',
            command_manager=CommandManager('cliff.demo'),
            )


def main():
    myapp = DemoApp()
    myapp.run(sys.argv[1:])
