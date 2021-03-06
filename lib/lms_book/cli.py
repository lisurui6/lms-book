import sys
from typing import List
from lms_book import LMSBookCommand, create_part, create_chapter, publish, pull, sync, LOGGER


def main():
    parse_commands(sys.argv)


def parse_command(command: LMSBookCommand, argv: List[str]):
    if command == LMSBookCommand.create:
        if argv[0].lower() == "part":
            create_part(*argv[1:])
        elif argv[0].lower() == "chapter":
            create_chapter(*argv[1:])
        else:
            raise ValueError("Create {} not supported. Can only create part or chapter at the moment.".format(argv[0]))
    if command == LMSBookCommand.pull:
        pull(*argv)
    if command == LMSBookCommand.publish:
        publish(*argv)
    if command == LMSBookCommand.sync:
        sync()


def parse_commands(argv=None):
    try:
        LOGGER.info(" Running command: {}".format(" ".join(argv)))
        command = LMSBookCommand.from_str(argv[1])
    except KeyError:
        raise KeyError(
            "Valid commands are create, pull, publish, and sync. Or you can run it interactively with -i option."
        )
    parse_command(command, argv[2:])
