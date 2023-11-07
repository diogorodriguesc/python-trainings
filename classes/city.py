import uuid

class City:
    def __init__(self, name, district, postalCode):
        self.__uuid = uuid.uuid4() # private
        self.name = name # public
        self.set_district(district)
        self.__set_postalCode(postalCode) # private

    def uuid(self):
        return self.__uuid

    def district(self): # public
        return self.__district

    def postalCode(self): # public
        return self.__postalCode

    def set_district(self, district): # public
        self.__district = district # private

    def __set_postalCode(self, postalCode): # public
        self.__postalCode = postalCode # private


city = City('Matosinhos', 'Porto', 4400)

print(city.uuid())
print(city.name)
print(city.district())
print(city.postalCode())

print(type(city.name))
print(type(city.district()))
print(type(city.postalCode()))

city.set_district('Aveiro')
print(city.district())

# city.__set_postalCode(4300) -> as __set_postalCode is private not accessible
