import definitions
from file_handler import FileHandler
from datetime import datetime
from dateutil.relativedelta import relativedelta


class Vehicles:
    vehicle_file_handler = FileHandler("vehicle")
    __vehicles = []

    def __init__(self):
        self.__vehicles = self.vehicle_file_handler.get_data()

    @classmethod
    def update_vehicle_by_id(cls, vehicle_id, **kwargs):
        valid_headers = definitions.file_data.get("vehicle").get("columns")
        for arg in kwargs:
            if arg not in valid_headers:
                return False
            else:
                cls.vehicle_file_handler.loop_through_and(FileHandler.update_csv, vehicle_id, kwargs)
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
print(vehicle.update_vehicle_by_id('1G6AB5R37D0832002', brand='Chevrolet', year="1994"))
# # print(vehicle.get_time_to_test('1G6AB5R37D0832002'))



