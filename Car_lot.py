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
        self.all_users = self.user_handler.load_dict_csv()
        self.__employees = [row for row in self.all_users if row['role'] == 'employee']

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
        self.user_handler.get_data()

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
            # add to vehicle csv file
            cls.vehicle_handler.append_to_csv_new(file_data[1:])
            # updated stored list of csv file data inside the class itself
            cls.__vehicles = cls.vehicle_handler.get_data()
            return True
        else:
            return False

    def get_fleet_size(self):
        return len(self.__vehicles)

    def get_all_cars_by_brand(self, brand):
        try:
            brand_pos = definitions.file_data.get("vehicle").get("columns").index("brand")
            wanted = [row for row in self.__vehicles if row[brand_pos] == brand]
            return len(wanted)
        except Exception as e:
            print("Error: " + str(e))

    def how_many_own_more_then_one_car(self):
        owner_pos = definitions.file_data.get("vehicle").get("columns").index("owner")
        file_data = self.vehicle_handler.load_from_csv()
        all_owners = [row[owner_pos] for row in file_data]
        owners_of_more_than_one_car = [name for name in all_owners if all_owners.count(name) > 1]
        # remove duplicate names
        return list(set(owners_of_more_than_one_car))

    # struggling here w/ kwargs
    def get_all_cars_by_filter(self, and_or="and", **kwargs):
        file_data = self.vehicle_handler.load_dict_csv()
        relevant_vehicles = []
        for key, value in kwargs.items():
            for row in file_data:
                if value == row[key]:
                    relevant_vehicles.append(row)
        return relevant_vehicles

    def does_employee_have_car(self, name):
        owner_pos = definitions.file_data.get("vehicle").get("columns").index("owner")
        brand_pos = definitions.file_data.get("vehicle").get("columns").index("brand")
        file_data = self.vehicle_handler.load_from_csv()
        search_employee = [row for row in file_data if row[owner_pos] == name]
        if len(search_employee) == 0:
            return False
        else:
            return f"Employee {name} owns a {search_employee[0][brand_pos]}"

    def all_employees_with_car(self):
        employees = []
        for employee in self.__employees:
            answer = self.does_employee_have_car(f"{employee['first_name']} {employee['last_name']}")
            if answer:
                employees.append(answer)
        return employees

    def get_all_employee_who_own_car_brand(self, brand):
        employees_with_brand = []
        employees_with_cars = self.all_employees_with_car()
        for employee in employees_with_cars:
            answer = self.get_all_cars_by_filter(name=employee, brand=brand)
            employees_with_brand.append(answer)
        return employees_with_brand


lot = CarLot()
print(lot.get_all_cars_by_filter(brand='Chevrolet'))
# print(lot.all_employees_with_car())



# Test cases Add to Fleet
# print(CarLot.add_to_fleet("fleet_missing_info.csv"))
# print(CarLot.add_to_fleet("fleet_same_order.csv"))
# print(CarLot.add_to_fleet("fleet_different_order.csv"))

# Test for fleet size
# print(lot.get_fleet_size())

# Test for get cars by brand
# print(lot.get_all_cars_by_brand("Chevrolet"))


