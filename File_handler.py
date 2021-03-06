from csv import reader
from csv import DictReader
from csv import DictWriter
from pathlib import Path
import os
import csv
from operator import itemgetter
import definitions


class FileHandler:
    __csv_data = None

    def __init__(self, file_name):
        if self.__csv_data is None:
            self.__csv_data = []
        main_dir = str(Path(__file__).parent)
        self.file_name = file_name
        self._csv_path = f"{main_dir}{os.sep}CSV{os.sep}{self.file_name}.csv"
        # get current info right away on instantiation
        self.load_from_csv()

    def get_data(self):
        return self.__csv_data

    def refresh_data(self):
        self.load_from_csv()

    def load_from_csv(self):
        try:
            self.__csv_data = []
            with open(self._csv_path) as file:
                csv_reader = reader(file)
                for row in csv_reader:
                    self.__csv_data.append(row)
        except FileNotFoundError:
            print("FileNotFoundError: No such file exists.")
        except OSError:
            print("OSError: Bad file descriptor. Type must be string.")

    # def load_dict_csv(self):
    #     try:
    #         with open(self._csv_path) as file:
    #             csv_reader = DictReader(file)
    #             return list(csv_reader)
    #     except FileNotFoundError:
    #         print("FileNotFoundError: No such file exists.")
    #     except OSError:
    #         print("OSError: Bad file descriptor. Type must be string.")

    def write_to_csv(self, updated_data):
        with open(self._csv_path, "w") as output:
            writer = csv.writer(output)
            for item in updated_data:
                writer.writerow(item)
        self.refresh_data()

    def append_multiple_to_csv(self, updated_data):
        with open(self._csv_path, "a") as output:
            writer = csv.writer(output)
            for item in updated_data:
                writer.writerow(item)
        self.refresh_data()

    def append_single(self, item):
        with open(self._csv_path, "a") as output:
            writer = csv.writer(output)
            writer.writerow(item)
        self.refresh_data()

    @staticmethod
    def data_join(**kwargs):
        pass

    def loop_through_and(self, func, user_id, new_data):
        current_data = [row for row in self.__csv_data]
        updated_data = func(self, self.__csv_data, user_id, new_data)
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

    def update_csv(self, file_data, id_num, new_data, new=False):
        all_items = []
        for row in file_data:
            if row[0] != id_num:
                all_items.append(row)
            else:
                for arg in new_data:
                    to_change = definitions.file_data.get(self.file_name).get("columns").index(arg)
                    row[to_change] = new_data.get(arg)
                all_items.append(row)
        return all_items

    # made to only sort files we already have stored (i.e.: user, vehicle, car_lot)
    def sort_by_key(self, key, direction="up"):
        reverse_val = False
        if direction == 'down':
            reverse_val = True
        try:
            key_pos = definitions.file_data.get(self.file_name).get("columns").index(key)
            return sorted(self.__csv_data, key=itemgetter(key_pos), reverse=reverse_val)
        except KeyError as e:
            print(f"{str(e)}: {key} not found.")
            return False
        except Exception as e:
            print("Error: " + str(e))


# Tests
# users = FileHandler("user.csv")
# print(users.sort_by_key("first_name"))
# print(users.sort_by_key("last_name"))
# print(users.sort_by_key("role"))
# print(users.loop_through_and(FileHandler.update_csv, '8ccfd062-a0c4-4570-a38d-1199c838248f', {'first_name': 'Sam', 'last_name': 'Korn'}))
