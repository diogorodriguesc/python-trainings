from dataclasses import dataclass

@dataclass
class City:
    name: str
    district: str
    postalCode: int
    active = 1

matosinhos = City('Matosinhos', 'Porto', 4400)
aveiro = City('Aveiro', 'Aveiro', 3000)

for city in [matosinhos, aveiro]:    
    print(city.name)
    print(city.district)
    print(city.postalCode)
    print(city.active)
