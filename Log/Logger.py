import datetime
import os
import threading
from pathlib import Path


class Logger:
    def __init__(self, file):
        self.file = file
        self._path = f"{Path(__file__).parent}{os.sep}{self.file}"

    # //every hour not working

    def add_to_log(self, msg):
        try:
            f = open(self._path, "a")
        except Exception as e:
            print(str(e))
        else:
            # threading.Timer(5.0, self.add_to_log).start()
            x = datetime.datetime.now()
            f.write(x.strftime("%d/%m/%y %H:%M:%S ") + msg + "\n")


# Tests
messages = Logger("msg_log.log")
# messages.add_to_log("test")
messages.add_to_log("success")
# messages.add_to_log("test three")
