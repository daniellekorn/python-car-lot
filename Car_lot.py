from csv import DictReader
from file_handler import FileHandler
import definitions
import collections


class CarLot:
    vehicle_handler = FileHandler("vehicle")
    user_handler = FileHandler("user")
    __users = []
    __vehicles = []
    __employees = []

    def __init__(self):
        self.__vehicles = self.vehicle_handler.get_data()
        self.__users = self.user_handler.get_data()

    def load_employee_data(self):
        role_pos = definitions.file_data.get("user").get("columns").index("role")
        self.user_handler.load_from_csv()
        all_users = self.user_handler.get_data()
        self.__employees = [row for row in all_users if row[role_pos] == 'employee']
        return self.__employees

    # need to return t/f and add error handling
    def update_salary_by_name(self, employee_salary, name):
        name = name.lower()
        all_employees = []
        found = False
        first_name_pos = definitions.file_data.get("user").get("columns").index("first_name")
        last_name_pos = definitions.file_data.get("user").get("columns").index("last_name")
        salary_pos = definitions.file_data.get("user").get("columns").index("salary")

        for row in self.__users:
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

    def add_to_fleet(self, external_csv_fleet_file):
        data = FileHandler(external_csv_fleet_file)
        data.load_from_csv()
        provided_details = data.get_data()[0]
        required_details = definitions.file_data.get("vehicle").get("columns")
        if collections.Counter(required_details) == collections.Counter(provided_details):
            # add to vehicle csv file
            self.vehicle_handler.append_multiple_to_csv(data.get_data()[1:])
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
        all_owners = [row[owner_pos] for row in self.__users]
        owners_of_more_than_one_car = [name for name in all_owners if all_owners.count(name) > 1]
        # remove duplicate names
        return list(set(owners_of_more_than_one_car))

    def get_all_cars_by_filter(self, and_or="and", **kwargs):
        if and_or == "or":
            matches = [row for row in self.__vehicles for k, v in kwargs.items() if v in row]
        else:
            matches = []
            for row in self.__vehicles:
                all_match = True
                for k, v in kwargs.items():
                    cur_key = definitions.file_data.get("vehicle").get("columns").index(k)
                    if row[cur_key].lower() != kwargs[k].lower():
                        all_match = False
                if all_match:
                    matches.append(row)
        return matches

    def does_employee_have_car(self, name):
        owner_pos = definitions.file_data.get("vehicle").get("columns").index("owner")
        brand_pos = definitions.file_data.get("vehicle").get("columns").index("brand")
        search_employee = [row for row in self.__vehicles if row[owner_pos] == name]
        if len(search_employee) == 0:
            return False
        else:
            return f"Employee {name} owns a {search_employee[0][brand_pos]}"

    def all_employees_with_car(self):
        employees = []
        self.load_employee_data()
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
# print(lot.load_employee_data())
# print(lot.does_employee_have_car('Aymer McKennan'))
# print(lot.get_all_cars_by_filter(brand='Honda'))
# print(lot.how_many_own_more_then_one_car())
print(lot.get_all_cars_by_filter(and_or="and", brand='Chevrolet', color="Black"))
# print(lot.update_salary_by_name(4254, 'Kaaskooper'))



# Tests
# print(lot.add_to_fleet("fleet_missing_info.csv"))
# print(lot.add_to_fleet("fleet_same_order.csv"))
# print(lot.add_to_fleet("fleet_different_order.csv"))
# print(lot.get_fleet_size())
# print(lot.get_all_cars_by_brand("Chevrolet"))



