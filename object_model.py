class Employee:
    def __init__(self, name, username, email, password, last_access):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.last_access_time = last_access

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



