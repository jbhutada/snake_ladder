class Cell:
    def __init__(self, id):
        self.id = id
        self.special_object = None
        self.special_object_type = None

    def assign_special_object(self, obj_type, obj):
        self.special_object_type = obj_type
        self.special_object = obj

    def make_special_move(self):
        # handle none objects

        return self.special_object.make_move()
