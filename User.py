from csv import DictReader
from file_handler import FileHandler


class User:
    user_file_handler = FileHandler("user.csv")
    _users = user_file_handler.get_data()

    def __init__(self, user_id, first, last, password):
        self._user_id = user_id
        self.first = first
        self.last = last
        self._password = password

    def __repr__(self):
        return f"User {self.first} {self.last}"

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        if isinstance(new_password, str):
            if self.__valid_password_length(new_password):
                self._password = new_password
            else:
                raise ValueError("Password must be between 4-12 characters")
        else:
            raise TypeError("Password must be type string")

    @staticmethod
    def __valid_password_length(password):
        length = len(password)
        if 4 < length < 12:
            return True
        else:
            return False

    @staticmethod
    def user_auth(name, password):
        try:
            with open("/CSV/User") as file:
                csv_reader = DictReader(file)
                for user in csv_reader:
                    if (name == user['last'] or name == user['first'] or name == user['first'] + " " + user['last']) \
                            and password == user['password']:
                        return f"User role: {user['role']}"
                    else:
                        continue
                return False
        except FileNotFoundError:
            print("FileNotFoundError: No such file exists.")
        except OSError:
            print("OSError: Bad file descriptor. Type must be string.")


print(User._users)