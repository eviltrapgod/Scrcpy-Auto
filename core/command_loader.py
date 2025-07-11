import json
import logging
import asyncio

from services.input_service import json_command_file

logger = logging.getLogger(__name__)


def json_command_list_load(self):

    with open(json_command_file, 'r') as f:
        command_list = json.load(f)
    return command_list

