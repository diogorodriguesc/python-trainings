import uuid

class Uuid:
    def __init__(self):
        self.__uuid = uuid.uuid4() # private
    
    def uuid(self):
        return self.__uuid
