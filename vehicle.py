import definitions
from file_handler import FileHandler


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


#
# print(Vehicles.update_vehicle_by_id("1B3CB9HA5BD797092", brand=1, myarg2="two", myarg3=3))
#



