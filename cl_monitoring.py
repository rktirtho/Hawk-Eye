
class Monitoring:
    def __init__(self, id, person_id, area,is_permitted,  time):
        self.id = id
        self.person_id = person_id
        self.area = area
        self.is_permitted = is_permitted
        self.time = time

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_person_id(self):
        return self.person_id

    def set_person_id(self, person_id):
        self.person_id = person_id

    def get_area(self):
        return self.area

    def set_area(self, area):
        self.area = area

    def is_permit(self):
        return self.is_permitted

    def set_permit(self, permit):
        self.is_permitted = permit

    def get_time(self):
        return self.time
    def set_time(self, time):
        self.time = time


