class Permitted:
    def __init__(self, name, image, organizaton, org_id, id= None):
        self.name = name
        self.image = image
        self.organizaton = organizaton
        self.org_id = org_id
        self.id = id

    def get_id(self):
        return self.id

    def set_id(self,id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name =name

    def get_organization(self):
        return self.organizaton

    def set_organization(self, org ):
        self.organizaton = org

    def get_org_id(self):
        return self.org_id

    def set_org_id(self, org_id):
        self.org_id = org_id

    # def get_(self):
    #     return self.
    #
    # def set_(self, ):
    #     self. =
    #
    # def get_(self):
    #     return self.
    #
    # def set_(self, ):
    #     self. =




