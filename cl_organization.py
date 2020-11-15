class Organization:
    def __init__(self, name, woner, address, id=None, reg_time =None):
        self.id = id
        self.name = name
        self.woner = woner
        self.address = address
        self.reg_time = reg_time

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_(self, name):
        self.name = name

    def get_woner(self):
        return self.woner

    def set_woner(self, woner):
        self.woner = woner

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_reg_time(self):
        return self.reg_time

    def set_reg_time(self, reg_time):
        self.reg_time

