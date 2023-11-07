import uuid

class Uuid:
    def __init__(self):
        self.__set_uuid()
    
    def uuid(self):
        return self.__uuid

    def _reset_uuid(self): # protected method
        self.__set_uuid()

    def __set_uuid(self): # private method
        self.__uuid = uuid.uuid4() # private