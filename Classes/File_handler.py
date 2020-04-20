from csv import reader
from csv import DictReader
from csv import DictWriter
from pathlib import Path
import os
import csv


class FileHandler:
    def __init__(self, file_name=""):
        main_dir = str(Path(__file__).parent.parent)
        self.file_name = file_name
        self._csv_path = f"{main_dir}{os.sep}CSV{os.sep}{self.file_name}"

    def load_from_csv(self):
        try:
            with open(self._csv_path) as file:
                csv_reader = DictReader(file)
                for row in csv_reader:
                    print(row)
        except FileNotFoundError:
            print("FileNotFoundError: No such file exists.")
        except OSError:
            print("OSError: Bad file descriptor. Type must be string.")

    def append_to_csv(self, data):
        with open(self._csv_path) as file:
            csv_reader = reader(file)
            file_data = list(csv_reader)
            existing_headers = file_data[0]
            existing_ids = []
            for item in file_data[1:]:
                existing_ids.append(item[0])
        with open(self._csv_path, "a") as file:
            try:
                csv_writer = DictWriter(file, fieldnames=existing_headers)
                if "user_id" not in data:
                    raise ValueError("ValueError: User must have valid ID")
                elif data["user_id"] in existing_ids:
                    raise ValueError("ValueError: ID taken. Provide new, valid user ID.")
                else:
                    csv_writer.writerow(data)
            except ValueError as e:
                return e

    @staticmethod
    def data_join(**kwargs):
        pass

    def loop_through_and(self, func, user_id):
        try:
            with open(self._csv_path) as inp:
                csv_reader = reader(inp)
                file_data = list(csv_reader)
        except FileNotFoundError:
            print("FileNotFoundError: Please input an appropriate path.")
        else:
            current_data = [row for row in file_data]
            updated_data = func(user_id, file_data)
            with open(self._csv_path, "w") as output:
                writer = csv.writer(output)
                for item in updated_data:
                    writer.writerow(item)
            if len(current_data) > len(updated_data):
                return True
            else:
                return False

    @staticmethod
    def remove_from_csv(user_id, file_data):
        updated_data = [row for row in file_data if row[0] != user_id]
        return updated_data


# def update_csv(user_id, row, file_data):
users = FileHandler("User")

# print(FileHandler.loop_through_and(FileHandler.remove_from_csv, "/Users/daniellekorn/PycharmProjects/car_lot/CSV/User", '5224f411-57aa-4dd2-9cfe-7b76cb92ae3c'))
