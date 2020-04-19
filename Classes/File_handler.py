from csv import DictReader


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
        pass


# Test
FileHandler.load_from_csv("/Users/daniellekorn/PycharmProjects/car_lot/CSV/User")
