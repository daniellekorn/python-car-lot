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
        self._csv_path = f"{main_dir}{os.sep}CSV{os.sep}{self.file_name}"

    def get_data(self):
        return self.__csv_data

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

    def load_dict_csv(self):
        try:
            with open(self._csv_path) as file:
                csv_reader = DictReader(file)
                return list(csv_reader)
        except FileNotFoundError:
            print("FileNotFoundError: No such file exists.")
        except OSError:
            print("OSError: Bad file descriptor. Type must be string.")

    def refresh_data(self):
        self.load_from_csv()

    def write_to_csv(self, updated_data):
        with open(self._csv_path, "w") as output:
            writer = csv.writer(output)
            for item in updated_data:
                writer.writerow(item)
        self.refresh_data()

    def write_dict_csv(self, data):
        with open(self._csv_path, 'w') as outfile:
            fp = csv.DictWriter(outfile, data[0].keys())
            fp.writeheader()
            fp.writerows(data)
        self.refresh_data()

    def append_to_csv_new(self, updated_data):
        with open(self._csv_path, "a") as output:
            writer = csv.writer(output)
            for item in updated_data:
                writer.writerow(item)
        self.refresh_data()

    @staticmethod
    def data_join(**kwargs):
        pass

    def loop_through_and(self, func, user_id, new_data=""):
        current_data = [row for row in self.__csv_data]
        updated_data = func(self.__csv_data, user_id, new_data)
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

    # made to only sort files we already have stored (i.e.: user, vehicle, car_lot)
    def sort_by_key(self, key):
        try:
            key_pos = definitions.file_data.get(self.file_name[:-4]).get("columns").index(key)
            return sorted(self.__csv_data, key=itemgetter(key_pos))
        except Exception as e:
            print("Error: " + str(e))

    def update_based_on_id(self, id_num, **kwargs):
        valid_headers = definitions.file_data.get("vehicle").get("columns")
        valid_values = [(key, kwargs[key]) for key in kwargs if key in valid_headers]
        all_vehicles = []
        other_vehicles = [row for row in self.__csv_data if row[0] != id_num]
        for row in self.__csv_data:
            if id_num == row[0]:
                for (key, value) in valid_values:
                    row[key] = value
                all_vehicles.append(row)
        all_vehicles.append(other_vehicles)
        print(all_vehicles)
    # cls.vehicle_file_handler.write_dict_csv(all_vehicles)


# Tests
users = FileHandler("user.csv")
users.update_based_on_id('944767c2-1b11-4dec-b87e-3666958a39f1')
# print(users.sort_by_key("first_name"))
# print(users.sort_by_key("last_name"))
# print(users.sort_by_key("role"))

