import datetime
import os
import threading
from pathlib import Path


class Logger:
    def __init__(self, file):
        self.file = file

    # //every hour not working
    def add_to_log(self, msg):
        try:
            # abs_time = print(os.path.getctime(self.file))
            # local_time = time.ctime(abs_time)
            # print(local_time)
            path = Path(f"//{__file__}")
            f = open(f"{path.parent}{os.sep}{self.file}", "a")
        except Exception as e:
            print(str(e))
        else:
            threading.Timer(5.0, self.add_to_log).start()
            x = datetime.datetime.now()
            f.write(x.strftime("%d/%m/%y %H:%M:%S ") + msg + "\n")
            print("working")


# Tests
messages = Logger("msg_log.log")
# messages.add_to_log("test")
messages.add_to_log()
# messages.add_to_log("test three")
