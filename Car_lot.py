from csv import DictReader
from file_handler import FileHandler
import definitions

class CarLot:
    vehicle_handler = FileHandler("vehicle")
    user_handler = FileHandler("user.csv")
    cars = []
    employee = []

    def __init__(self):
        self._vehicles = self.vehicle_handler.get_data()

    def load_car_data(self, *args):
        pass

    def load_employee_data(self, *args):
        pass

    # need to return t/f and add error handling
    def update_salary_by_name(self, employee_salary, name):
        first_name_pos = definitions.file_data.get("user").get("columns").index("first_name")
        last_name_pos = definitions.file_data.get("user").get("columns").index("last_name")
        salary_pos = definitions.file_data.get("user").get("columns").index("salary")
        name = name.lower()

        file_data = self.user_handler.load_from_csv()
        all_employees = []
        found = False
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



# CarLot.add_to_fleet("/Users/daniellekorn/Downloads/mock.csv")
lot = CarLot()
# print(lot.update_salary_by_name(56, 'sam'))
# print(lot.update_salary_by_name(54, 'dorgon'))
# lot.get_fleet_size("/Users/daniellekorn/Downloads/mock.csv")
