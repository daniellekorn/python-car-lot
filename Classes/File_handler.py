from csv import reader
from csv import DictReader
from csv import DictWriter
import csv
import os
from pathlib import Path
import os


class FileHandler:
    def __init__(self, file_name=""):
        self.file_name = file_name
        self.cur_dir = os.getcwd()

    @staticmethod
    def load_from_csv(file_name):
        try:
            with open(file_name) as file:
                csv_reader = DictReader(file)
                for row in csv_reader:
                    print(row)
        except FileNotFoundError:
            print("FileNotFoundError: No such file exists.")
        except OSError:
            print("OSError: Bad file descriptor. Type must be string.")

    @staticmethod
    def append_to_csv(file_name, data):
        with open(file_name) as file:
            csv_reader = reader(file)
            file_data = list(csv_reader)
            existing_headers = file_data[0]
            existing_ids = []
            for item in file_data[1:]:
                existing_ids.append(item[0])
        with open(file_name, "a") as file:
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

    @staticmethod
    def loop_through_and(self, file_name, func, *args):
        with open(file_name) as file:
            csv_reader = reader(file)
            for row in csv_reader:
                func(row, *args)

    @staticmethod
    def remove_from_csv(file_name, user_id):
        try:
            with open(file_name) as inp:
                csv_reader = reader(inp)
                file_data = list(csv_reader)
        except FileNotFoundError:
            print("FileNotFoundError: Please input an appropriate path.")
        else:
            current_data = [row for row in file_data]
            updated_data = [row for row in file_data if row[0] != user_id]
            with open(file_name, "w") as output:
                writer = csv.writer(output)
                for item in updated_data:
                    writer.writerow(item)
                # checks if id was found and deleted properly
            if len(current_data) > len(updated_data):
                return True
            else:
                return False


