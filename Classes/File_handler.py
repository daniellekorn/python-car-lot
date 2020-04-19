from csv import reader
from csv import DictReader
from csv import writer, DictWriter


class FileHandler:
    def __init__(self):
        pass

    @staticmethod
    def load_from_csv(file_name):
        try:
            with open(file_name) as file:
                csv_reader = DictReader(file)
                for row in csv_reader:
                    print(row)
        except FileNotFoundError:
            print("FileNotFoundError: No such file exists.")
        except OSError:
            print("OSError: Bad file descriptor. Type must be string.")

    @staticmethod
    def append_to_csv(file_name, data):
        with open(file_name) as file:
            csv_reader = reader(file)
            existing_headers = list(csv_reader)[0]
        with open(file_name, "a", newline='') as file:
            try:
                csv_writer = DictWriter(file, fieldnames=existing_headers)
                csv_writer.writerow(data)
            except ValueError as e:
                return e


# Test
# FileHandler.load_from_csv("/Users/daniellekorn/PycharmProjects/car_lot/CSV/User")
FileHandler.append_to_csv("/Users/daniellekorn/PycharmProjects/car_lot/CSV/User", {
                "first": "Garfield"
})
