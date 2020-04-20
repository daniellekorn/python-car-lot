from csv import DictReader


class CarLot:
    size = 0
    cars = []
    employee = []

    def load_car_data(self, *args):
        pass

    def load_employee_data(self, *args):
        pass

    # put filler N/A if nothing -- put to vehicle csv
    @classmethod
    def add_to_fleet(cls, external_csv_fleet_file):
        required_details = "id, brand, owner, last_test, color, door_count"
        line_num = 0
        with open(external_csv_fleet_file) as file:
            csv_reader = DictReader(file, delimiter=',')
            # get the headers provided
            for row in csv_reader:
                if line_num == 0:
                    provided_details = ", ".join(row)

            # ensure data in proper format (correct headers)
            if required_details == provided_details:
                print("success")
            else:
                print("failure")

            # if proper data, append to cls cars list
            for row in csv_reader:
                if line_num == 0:
                    continue
                else:
                    cls.cars.append(row)


CarLot.add_to_fleet("/Users/daniellekorn/Downloads/mock.csv")