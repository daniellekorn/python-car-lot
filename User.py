from csv import DictReader
from file_handler import FileHandler
import definitions


class User:
    user_file_handler = FileHandler("user.csv")
    __users = None
    num_users = 0

    def __init__(self):
        if self.__users is None:
            self.__users = []
        self.__users = self.user_file_handler.get_data()
        # think I want to move this to separate class:
        # self._user_id = user_id
        # self.first = first
        # self.last = last
        # self._password = password

    def __repr__(self):
        return f"Obj holding {self.num_users} users"

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

    def load_current_users(self):
        return self.user_file_handler.load_from_csv()

    def user_auth(self, name, password):
        try:
            first_name_pos = definitions.file_data.get("user").get("columns").index("first_name")
            last_name_pos = definitions.file_data.get("user").get("columns").index("last_name")
            password_pos = definitions.file_data.get("user").get("columns").index("password")
            role_pos = definitions.file_data.get("user").get("columns").index("role")

            for user in self.__users:
                if (name == user[last_name_pos] or name == user[first_name_pos] or name == user[first_name_pos] +
                        " " + user[last_name_pos]) and password == user[password_pos]:
                    return f"User role: {user[role_pos]}"
                else:
                    continue
            return False
        except FileNotFoundError:
            print("FileNotFoundError: No such file exists.")
        except OSError:
            print("OSError: Bad file descriptor. Type must be string.")

    @classmethod
    def add_user(cls, user_id, **kwargs):
        valid_headers = definitions.file_data.get("user").get("columns")
        valid_values = [(key, kwargs[key]) for key in kwargs if key in valid_headers]
        file_data = cls.user_file_handler.load_dict_csv()
        all_users = []
        other_users = [row for row in file_data if row['user_id'] != user_id]
        for row in file_data:
            if user_id == row['user_id']:
                for (key, value) in valid_values:
                    row[key] = value
                all_users.append(row)
        all_users.append(other_users)
        # need to write back to csv here


users = User()
users.load_current_users()
# User.add_user(user_id='98082ed5-54f4-468b-adac-b089fe3438b6', first_name="Danielle", last_name="Korn")
