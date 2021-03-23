import argparse
import textwrap

from west import log
from west.commands import WestCommand, CommandError

class Hello(WestCommand):

    def __init__(self):
        super(Hello, self).__init__(
            'hello',  # gets stored as self.name
            'says hello',  # self.help
            # self.description:
            textwrap.dedent('''
            Very simple command, not much here'''))

    def do_add_parser(self, parser_adder):
        parser = parser_adder.add_parser(
            self.name,
            help=self.help,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=self.description)
        return parser

    def do_run(self, args, extra):
        log.banner("Hello!")

