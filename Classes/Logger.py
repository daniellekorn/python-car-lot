import datetime
from logging.handlers import TimedRotatingFileHandler


class Logger:
    def __init__(self, path):
        self._path = path

    def add_to_log(self, msg):
        try:
            f = open(self._path, "a")
        except Exception as e:
            print("Something went wrong: " + str(e))
        else:
            x = datetime.datetime.now()
            f.write(x.strftime("%d/%m/%y %H:%M:%S ") + msg + "\n")


messages = Logger("/Users/daniellekorn/PycharmProjects/car_lot/msg_log.log")
messages.add_to_log("test")
messages.add_to_log("test two")
messages.add_to_log("test three")