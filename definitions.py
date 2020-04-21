import pathlib
import os

file_data = {
    "user": {
        "file_name": "user.csv",
        "columns": ("user_id", "first_name", "last_name", "password", "position", "salary", "role")
    },
    "vehicle": {
        "file_name": "vehicle.csv",
        "columns": ("id", "brand", "owner", "last_test", "color", "door_count", "year")
    },
    "car_lot": {
        "file_name": "car_lot.csv",
        "columns": ("id", "employees", "vehicles")
    }
}

# logger definitions
log_dir = str(pathlib.Path(__file__).parent) + os.sep + "log"
time_msg_format = "%m-%d-%Y, %H:%M:%S"
time_file_format = "%H_%M_%S"