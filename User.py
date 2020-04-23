from csv import DictReader
from file_handler import FileHandler
import definitions
import json


class User:
    user_file_handler = FileHandler("user")
    __users = None
    num_users = 0

    def __init__(self):
        if self.__users is None:
            self.__users = []
        self.__users = self.user_file_handler.get_data()

    def __repr__(self):
        return f"Obj holding {self.num_users} users"

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

    def add_user(self, user_id, **kwargs):
        valid_headers = definitions.file_data.get("user").get("columns")
        for i in self.__users:
            if i[0] == user_id:
                raise ValueError("User Id taken")
        for arg in kwargs:
            if arg not in valid_headers:
                return False
            elif len(kwargs) < len(valid_headers) - 1:
                return False
            else:
                print(self.__users)
                user = [kwargs.get(arg) for arg in kwargs]
                user.insert(0, user_id)
                self.user_file_handler.append_single(user)
            return True


users = User()
# print(users.add_user('98082ed5-54f4-468b-adac-b089fe38b6', first_name="Tom", last_name="Rittler", password="jfsdfnad",
#                     position="doorman", salary=3434, role="employee"))
