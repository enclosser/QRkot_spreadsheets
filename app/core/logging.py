import logging
from logging.handlers import RotatingFileHandler

LOG_FORMAT = '%(asctime)s, %(levelname)s, %(message)s, %(name)s'
FILENAME = 'aplication.log'


logging.basicConfig(format=LOG_FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler(FILENAME, maxBytes=50000000, backupCount=2)
logger.addHandler(handler)
