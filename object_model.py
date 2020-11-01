import datetime
class Employee:
    def __init__(self, id, name, username, email, password):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.last_access_time = datetime.datetime.now()
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.name = username

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.name = email

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.name = password

    def get_last_access(self):
        return self.last_access_time

    def set_last_access(self, last_access):
        self.name = last_access



