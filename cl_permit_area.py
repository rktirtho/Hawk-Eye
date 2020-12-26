class PermitArea:
    def __init__(self, emp_id, area, id= None):
        self.id = id
        self.emp_id = emp_id
        self.area=area

    def defget_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_emp_id(self):
        return self.emp_id

    def set_emp_id(self, emp_id):
        self.emp_id = emp_id

    def get_area(self):
        return self.area

    def set_area(self, area):
        self.area = area



