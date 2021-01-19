
class Stranger:
    def __init__(self, id, image, time, visited = None):
        self.id = id
        self.image = image
        self.time = time
        self.visited = visited

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_image(self):
        return self.image

    def set_image(self,image):
        self.image = image

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time

    def get_visited(self):
        return self.visited

    def set_visited(self, visited):
        self.visited = visited

