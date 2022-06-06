import logging
import constants

class logging_manager:
    def __init__(self):
        logging.basicConfig(
        level=logging.INFO,
        format=constants.LOGGING_FORMAT,
        handlers=[
            logging.FileHandler(constants.LOGGING_FILENAME),
            logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    
    def debug(self, msg):
        self.logger.debug(msg)


    def info(self, msg):
        self.logger.info(msg)


    def warning(self, msg):
        self.logger.warning(msg)


    def error(self, msg):
        self.logger.error(msg)

