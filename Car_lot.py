from csv import DictReader
from file_handler import FileHandler


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

    def update_salary_by_name(self, employee_salary, name):
        file_data = self.user_handler.get_data()
        print(file_data)
        for row in file_data:
            try:
                updated_data = []
                if row[2] == name or f"{row[1]} {row[2]}" != name:
                    updated_data.append(row)
                else:
                    employee_raise = [item if index != 5 else employee_salary for index, item in enumerate(row)]
                    updated_data.append(employee_raise)
                    self.user_handler.write_to_csv(updated_data)
                return True
            except IndexError as e:
                print("IndexError: " + str(e))




# CarLot.add_to_fleet("/Users/daniellekorn/Downloads/mock.csv")
lot = CarLot()
print(lot.update_salary_by_name(56, 'sam'))
print(lot.update_salary_by_name(54, 'Capnerhurst'))

