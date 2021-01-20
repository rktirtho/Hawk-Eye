
class Monitoring:
    def __init__(self, id, person_id, area, is_permitted,  time):
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

class StrangerMonitoring:
    def __init__(self, id, st_id, area,  time):
        self.id = id
        self.st_id = st_id
        self.area = area
        self.time = time

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_st_id(self):
        return self.st_id

    def set_st_id(self, st_id):
        self.st_id = st_id

    def get_area(self):
        return self.area

    def set_area(self, area):
        self.area = area



    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time

class Access:
    def __init__(self, id, name, org_id, image_id, time):
        self.id = id
        self.name = name
        self.org_id = org_id
        self.image_id = image_id
        self.time = time

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_org_id(self):
        return self.org_id

    def set_org_id(self, org_id):
        self.org_id =org_id

    def get_image_id(self):
        return self.image_id

    def set_(self, image_id):
        self.image_id =image_id

    def get_time(self):
        return self.time

    def set_(self, time):
        self.time = time





