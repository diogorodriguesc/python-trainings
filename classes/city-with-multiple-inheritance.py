from uuid_test import Uuid;
from value import Value;

class City(Uuid, Value):
    def __init__(self, name: str, district: str, postalCode: str, population: int):
        Uuid.__init__(self) # Constructor for Uuid
        Value.__init__(self, name) # Constructor for Value
        self.set_district(district)
        self.__set_postalCode(postalCode) # private
        self.__population = population

    def __len__(self): # Overwriting len for this object
        return self.__population

    def __repr__(self):
        return "Uuid: %s Value: %s" % (self.uuid(), self.value())

    def __str__(self):
        return self.value()

    def district(self) -> str: # public
        return self.__district

    def postalCode(self) -> int: # public
        return self.__postalCode

    def set_district(self, district) -> None: # public
        self.__district = district # private

    def __set_postalCode(self, postalCode) -> None: # public
        self.__postalCode = postalCode # private


city = City('Matosinhos', 'Porto', 4400, 1500000)

print(city.uuid())
print(city.value())
print(city.district())
print(city.postalCode()) 

print(type(city.value())) # Outputs: <class 'str'>
print(type(city.district())) # Outputs: <class 'str'>
print(type(city.postalCode())) # Outputs: <class 'int'>

city.set_district('Aveiro')
print(city.district()) # Outputs: Aveiro

# city.__set_postalCode(4300) -> as __set_postalCode is private not accessible

print(len(city)) # Outputs: 1500000
print(city) # Outputs: Matosinhos
print([city]) # Outputs: [Uuid: 22365a2d-3c43-4791-982a-444be4e92a93 Value: Matosinhos]
