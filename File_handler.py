from csv import reader
from csv import DictWriter
from pathlib import Path
import os
import csv


class FileHandler:
    __csv_data = None

    def __init__(self, file_name=""):
        if self.__csv_data is None:
            self.__csv_data = []
        main_dir = str(Path(__file__).parent)
        self.file_name = file_name
        self._csv_path = f"{main_dir}{os.sep}CSV{os.sep}{self.file_name}"

    def get_data(self):
        return self.__csv_data

    def load_from_csv(self):
        try:
            with open(self._csv_path) as file:
                csv_reader = reader(file)
                file_data = list(csv_reader)
                for row in file_data:
                    self.__csv_data.append(row)
                return file_data
        except FileNotFoundError:
            print("FileNotFoundError: No such file exists.")
        except OSError:
            print("OSError: Bad file descriptor. Type must be string.")

    def write_to_csv(self, updated_data):
        with open(self._csv_path, "w") as output:
            writer = csv.writer(output)
            for item in updated_data:
                writer.writerow(item)

    def append_to_csv(self, data):
        file_data = self.load_from_csv()
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

    def loop_through_and(self, func, user_id, new_data=""):
        try:
            file_data = self.load_from_csv()
        except FileNotFoundError:
            print("FileNotFoundError: Please input an appropriate path.")
        else:
            current_data = [row for row in file_data]
            updated_data = func(file_data, user_id, new_data)
            self.__csv_data = [item for item in updated_data]
            self.write_to_csv(updated_data)
            if updated_data != current_data:
                return True
            else:
                return False

    @staticmethod
    def remove_from_csv(file_data, user_id, new_data=""):
        updated_data = [row for row in file_data if row[0] != user_id]
        return updated_data

    @staticmethod
    def update_csv(file_data, user_id, new_data):
        not_matching_members = [row for row in file_data if row[0] != user_id]
        wanted_user = [row for row in file_data if row[0] == user_id]
        if wanted_user:
            revised_user = [user_id, new_data]
            not_matching_members.append(revised_user)
            return not_matching_members



# # Test
# users = FileHandler("user")
# print(users._csv_path)
# print(users.loop_through_and(FileHandler.remove_from_csv, '0f9860b0-502f-448e-9899-0017b5f81450', "hello"))
