class User:

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
            if (len(new_password) > 4) and (len(new_password) < 12):
                self._password = new_password
            else:
                raise ValueError("Password must be between 4-12 characters")
        else:
            raise TypeError("Password must be type string")

    @classmethod
    def user_auth(cls, name, password):
        # //check if user in csv file
        # //if so return "role"
        # //if not, return false