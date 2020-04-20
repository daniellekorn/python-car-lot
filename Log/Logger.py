import datetime
import os
import logging
from logging.handlers import TimedRotatingFileHandler


class Logger:
    def __init__(self, file):
        self.file = file

    def add_to_log(self, msg):
        try:
            log_dir = os.path.dirname(os.path.realpath(__file__))
            path = f"{log_dir}{os.sep}{self.file}"
            print(path)
            f = open(path, "a")
        except Exception as e:
            print(str(e))
        else:
            x = datetime.datetime.now()
            f.write(x.strftime("%d/%m/%y %H:%M:%S ") + msg + "\n")


# Tests
messages = Logger("msg_log.log")
messages.add_to_log("test")
messages.add_to_log("test two")
messages.add_to_log("test three")
