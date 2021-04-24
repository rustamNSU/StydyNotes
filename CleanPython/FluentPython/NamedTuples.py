from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP',  36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo[1], tokyo.population, tokyo.coordinates)
print("City._fields =", City._fields)

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print('delhi._asdict() = ', delhi._asdict())

for key, value in delhi._asdict().items():
    print(key + ':', value)