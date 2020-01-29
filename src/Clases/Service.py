from Clases.Helpers import Helpers
from Clases.QLDBDriver import QLDBDriver
from Clases.Password import Password

class Service():

    def __init__(self):
        self.password = Password()
        self.db = QLDBDriver()

    def validate_user(self, user, password):
        user_data = self.get_user(user)
        if user_data is None:
            return False

        user_password = user_data["password"]
        valid = self.password.verify_password(user_password, password)

        if not valid:
            return False

        return True

    def create_user(self, user, password):
        password_hash = self.password.hash_password(password)
        data_to_save = {
            "username" : user,
            "password" : password_hash
        }
        self.db.create_insert("users", data_to_save)


    def get_user(self, username):
        query = "SELECT * FROM users WHERE username = '{}'".format(username)
        data = self.db.create_query(query)
        if len(data) > 0:
            return data[0]
        return None

    def save_ws_log(self, request, response):
        data_to_save = {
            "request": Helpers.remove_special(request),
            "response": Helpers.remove_special(response)
        }
        self.db.create_insert("ws_log", data_to_save)