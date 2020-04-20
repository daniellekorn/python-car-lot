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
            file_data = list(csv_reader)
            existing_headers = file_data[0]
            existing_ids = []
            for item in file_data[1:]:
                existing_ids.append(item[0])
        with open(file_name, "a") as file:
            try:
                csv_writer = DictWriter(file, fieldnames=existing_headers)
                if "user_id" not in data:
                    raise ValueError("ValueError: User must have valid ID")
                elif data["user_id"] in existing_ids:
                    raise ValueError("ValueError: ID taken. Provide new, valid user ID.")
                else:
                    csv_writer.writerow(data)
            except ValueError as e:
                return e

    @staticmethod
    def data_join(**kwargs):
        pass


# Test for load
# FileHandler.load_from_csv("/Users/daniellekorn/PycharmProjects/car_lot/CSV/User")

# Tests for append
print(FileHandler.append_to_csv("/Users/daniellekorn/PycharmProjects/car_lot/CSV/User", {
                "user_id": "b54d22f0-8b80-491f-979a-5dd1a1c15253",
                "first": "Garfield",
                "last": "Binton",
                "password": "c2VP9QhHu8c1"
}))
print(FileHandler.append_to_csv("/Users/daniellekorn/PycharmProjects/car_lot/CSV/User", {
                "user_id": "b34d22d0-8b80-491f-979a-5dd1a1c15253",
                "first": "Samuel",
                "last": "Berger",
                "password": "c2VP9QhHu8c1"
}))
