import logging

logger = logging.getLogger(__name__)

class operation:
    def __init__(self, file_name, operation):
        self.operation = operation
        self.file_anem = file_name
