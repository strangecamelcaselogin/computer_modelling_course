import sys
from logging import getLogger, StreamHandler
# from logging.handlers import RotatingFileHandler


logger = getLogger('app')
logger.addHandler(StreamHandler(sys.stdout))
