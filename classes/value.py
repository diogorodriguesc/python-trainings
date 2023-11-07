class Value:
    def __init__(self, value):
        self.__value = value

    def value(self):
        return self.__value
    
    def _set_value(self, value):
        self.__value = value