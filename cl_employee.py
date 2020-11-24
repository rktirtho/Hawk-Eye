

class Employee:
    def __init__(self, name, username, email, password, org_id, join_date=None, id=None, last_excess=None):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.org_id = org_id
        self.join_date = join_date
        self.last_excess = last_excess

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def set_org_id(self, org_id):
        self.org_id = org_id

    def get_org_id(self):
        return self.org_id

    def set_join_date(self, join_date):
        self.join_date = join_date

    def get_join_date(self):
        return self.join_date

    def set_last_excess(self, last_excess):
        self.last_excess = last_excess

    def get_last_excess(self):
        return self.last_excess
