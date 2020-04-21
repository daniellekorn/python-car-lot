from csv import DictReader
from file_handler import FileHandler
import definitions
import collections


class CarLot:
    vehicle_handler = FileHandler("vehicle.csv")
    user_handler = FileHandler("user.csv")
    __vehicles = []
    __employees = []

    def __init__(self):
        self.__vehicles = self.vehicle_handler.get_data()

    def load_car_data(self, *args):
        pass

    def load_employee_data(self, *args):
        pass

    # need to return t/f and add error handling
    def update_salary_by_name(self, employee_salary, name):
        name = name.lower()
        all_employees = []
        found = False
        first_name_pos = definitions.file_data.get("user").get("columns").index("first_name")
        last_name_pos = definitions.file_data.get("user").get("columns").index("last_name")
        salary_pos = definitions.file_data.get("user").get("columns").index("salary")
        file_data = self.user_handler.load_from_csv()

        for row in file_data:
            if row[last_name_pos].lower() == name or f"{row[first_name_pos]} {row[last_name_pos]}".lower() == name:
                found = True
                new_data = [item if index != salary_pos else employee_salary for index, item in enumerate(row)]
                all_employees.append(new_data)
            else:
                all_employees.append(row)
        # user file handler class to write updated info to csv
        self.user_handler.write_to_csv(all_employees)
        # checks if employee successfully given raise

        if found:
            return True
        else:
            return False

    @classmethod
    def add_to_fleet(cls, external_csv_fleet_file):
        data = FileHandler(external_csv_fleet_file)
        file_data = data.load_from_csv()
        required_details = definitions.file_data.get("vehicle").get("columns")
        provided_details = file_data[0]
        if collections.Counter(required_details) == collections.Counter(provided_details):
            cls.vehicle_handler.append_to_csv_new(file_data[1:])
            return True
        else:
            return False

# # Test cases Add to Fleet
# lot = CarLot()
# print(CarLot.add_to_fleet("fleet_missing_info.csv"))
# print(CarLot.add_to_fleet("fleet_same_order.csv"))
# print(CarLot.add_to_fleet("fleet_different_order.csv"))

