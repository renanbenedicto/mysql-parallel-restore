# -*- coding: utf-8 -*-

import logging, datetime, sys

class Log:
   def __init__(self, filename='mysql-parallel-restore'):

       self.logger = logging.getLogger(filename)
       self.logger.setLevel(logging.DEBUG)
       # handler = logging.StreamHandler(sys.stdout)
       handler = logging.FileHandler(filename + '.log')
       handler.setFormatter(logging.Formatter('%(message)s'))
       self.logger.addHandler(handler)

   def userFiles(self, message):
       self.logger.info(message)

   def debug(self, message):
       self.logger.debug(self.__format_log__('DEBUG', message))

   def info(self, message):
       self.logger.info(self.__format_log__('INFO', message))

   def warning(self, message):
       self.logger.warning(self.__format_log__('WARNING', message))

   def error(self, message):
       self.logger.error(self.__format_log__('ERROR', message))

   def critical(self, message):
       self.logger.critical(self.__format_log__('CRITICAL', message))

   def __format_log__(self, level, message):
       date=datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
       return '%s [%s] - %s' % (date, level, message)

   def __convert__(self, o):
       if isinstance(o, datetime.datetime):
           return o.__str__()
