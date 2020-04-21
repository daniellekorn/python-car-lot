import definitions
from file_handler import FileHandler
from datetime import datetime
from dateutil.relativedelta import relativedelta


class Vehicles:
    vehicle_file_handler = FileHandler("vehicle.csv")
    __vehicles = []

    def __init__(self):
        self.__vehicles = self.vehicle_file_handler.get_data()

    @classmethod
    def update_vehicle_by_id(cls, vehicle_id, **kwargs):
        valid_headers = definitions.file_data.get("vehicle").get("columns")
        valid_values = [(key, kwargs[key]) for key in kwargs if key in valid_headers]
        file_data = cls.vehicle_file_handler.load_dict_csv()
        all_vehicles = []
        other_vehicles = [row for row in file_data if row['id'] != vehicle_id]
        for row in file_data:
            if vehicle_id == row['id']:
                for (key, value) in valid_values:
                    row[key] = value
                all_vehicles.append(row)
        all_vehicles.append(other_vehicles)
        # cls.vehicle_file_handler.write_dict_csv(all_vehicles)
        return True

    # Google claims car should be tested every year, so this func returns date one year from last test
    def get_time_to_test(self, vehicle_id):
        test_pos = definitions.file_data.get("vehicle").get("columns").index("last_test")
        file_data = self.vehicle_file_handler.load_from_csv()
        last_test = [row[test_pos] for row in file_data if vehicle_id == row[0]]
        if len(last_test) == 0:
            return False
        else:
            last_test_date = datetime.strptime(str(last_test[0]), "%m/%d/%Y")
            next_test_date = last_test_date + relativedelta(years=1)
            return datetime.strftime(next_test_date, "%m/%d/%Y")


vehicle = Vehicles()
print(vehicle.get_time_to_test('1G6AB5R37D0832002'))
# print(Vehicles.update_vehicle_by_id("1B3CB9HA5BD797092", brand=1, myarg2="two", myarg3=3))
#



