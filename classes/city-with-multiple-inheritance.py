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

print(type(city.value()))
print(type(city.district()))
print(type(city.postalCode()))

city.set_district('Aveiro')
print(city.district())

# city.__set_postalCode(4300) -> as __set_postalCode is private not accessible

print(len(city))