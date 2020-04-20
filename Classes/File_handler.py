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

    def loop_through_and(self, func, user_id, new_data=""):
        try:
            with open(self._csv_path) as inp:
                csv_reader = reader(inp)
                file_data = list(csv_reader)
        except FileNotFoundError:
            print("FileNotFoundError: Please input an appropriate path.")
        else:
            current_data = [row for row in file_data]
            updated_data = func(file_data, user_id, new_data)
            # with open(self._csv_path, "w") as output:
            #     writer = csv.writer(output)
            #     for item in updated_data:
            #         writer.writerow(item)
            # if len(current_data) > len(updated_data):
            #     return True
            # else:
            #     return False

    @staticmethod
    def remove_from_csv(file_data, user_id, new_data):
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


users = FileHandler("User")
print(users.loop_through_and(FileHandler.update_csv, 'af364e96-3d68-4609-9cfd-641b4e2062f0', "hello"))
