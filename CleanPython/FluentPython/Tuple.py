"""
Examples of tuple (iterable) unpacking
"""

import os
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates
print(latitude, longitude)

t = (20, 8)
quotient, remainder = divmod(*t)
print(quotient, remainder)

_, filename = os.path.split('/home/rustam/.ssh/id_rsa.pub')
print(filename)


a, b, *rest = range(5)
print(a, b, rest)


a, b, *rest = range(2)
print(a, b, rest)


a, *body, c, d = range(5)
print(a, body, c, d)


*head, b, c, d = range(3)
print(head, b, c, d)


metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))
