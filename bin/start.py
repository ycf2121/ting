import sys,os
path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

# from conf import settings
# import logging.config
# logging.config.dictConfig(settings.LOGGING_DIC)
# my_logger=logging.getLogger('bank')
# my_logger.info('银行')

from core import src
if __name__ == '__main__':
    src.run()
