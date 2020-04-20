import datetime
import os
from pathlib import Path


class Logger:
    def __init__(self, file):
        self.file = file

    def add_to_log(self, msg):
        try:
            path = Path(f"//{__file__}")
            f = open(f"{path.parent}{os.sep}{self.file}", "a")
        except Exception as e:
            print(str(e))
        else:
            x = datetime.datetime.now()
            f.write(x.strftime("%d/%m/%y %H:%M:%S ") + msg + "\n")


# Tests
messages = Logger("msg_log.log")
messages.add_to_log("test")
# messages.add_to_log("test two")
# messages.add_to_log("test three")
