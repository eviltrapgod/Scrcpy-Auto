import logging

logger = logging.getLogger(__name__)


class Command:
    def __init__(self, command=None, description=None, name=None):
        self.command = command
        self.command_name = name
        self.command_desc = description
