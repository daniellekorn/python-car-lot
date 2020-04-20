import datetime
import logging
from logging.handlers import TimedRotatingFileHandler


class Logger:
    def __init__(self, path):
        self._path = path

    def add_to_log(self, msg):
        try:
            f = open(self._path, "a")
        except Exception as e:
            print(str(e))
        else:
            x = datetime.datetime.now()
            f.write(x.strftime("%d/%m/%y %H:%M:%S ") + msg + "\n")


messages = Logger("/Users/daniellekorn/PycharmProjects/car_lot/msg_log.log")
messages.add_to_log("test")
messages.add_to_log("test two")
messages.add_to_log("test three")


# import datetime
# import logging
# from logging.handlers import TimedRotatingFileHandler
#
#
# class Logger:
#     def __init__(self, path):
#         self._path = path
#
#     def add_to_log(self, msg):
#         logger = logging.getLogger(__name__)
#         logger.setLevel(logging.INFO)
#
#         try:
#             handler = TimedRotatingFileHandler(self._path, when="D", backupCount=24)
#             logger.addHandler(handler)
#         except Exception as e:
#             print("Something went wrong: " + str(e))
#         else:
#             x = datetime.datetime.now()
#             logger.info(x.strftime("%d/%m/%y %H:%M:%S ") + msg + "\n")
#
#             logger = logging.getLogger(__name__)
#             logger.setLevel(logging.INFO)
