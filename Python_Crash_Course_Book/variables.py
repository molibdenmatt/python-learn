"""
Naming conventions:
1_message - invalid name. Can't start from digit
message_1 - correct
_message_1 - correct
GRAVITY - naming a constant
camelCaseNamingMethods - For Class Names
snake_case - for everything else
"""

# TEXT

name = 'matt molibden'
print(name.title())
print(name.upper())
print(name.lower())

print("\tPython")  # tab
print("\nPython")  # new line

name = " Python "
print(name.strip())  # or lstrip() or rstrip()

# NUMBERS

age = 23
print(str(age))
age = "23"
print(int(age))

# LISTS

"""
Lists are ordered
Lists are mutable
Numeration starts from 0
"""
motorcycles = ['suzuki', 'ducati', 'yamaha']
motorcycles.append('bmw')
print(motorcycles)
print(motorcycles[0])
motorcycles.insert(0, 'honda')
print(motorcycles)

del motorcycles[0]
last_from_motorcycles = motorcycles.pop()
first_from_motorcycles = motorcycles.pop(0)
print(first_from_motorcycles)
motorcycles.remove('ducati')  # removes only the first occurrence of element from the list

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()  # Alphabetic sort
cars.sort(reverse=True)

cars_sorted = sorted(cars)  # Temporary sort
cars_reverse_sorted = sorted(cars, reverse=True)

print(len(cars_sorted))  # List length
cars_copy = cars[:]  # Easy way to make a copy of a list

# SLICES
print('slice:')
print(cars[0:2])  # [1:2:3] => from:to:step; can use negative values

"""
TUPLE
Tuple is immutable but we can reassign the tuples value
Tuple is ordered
"""
# Creating a tuple:
dimensions = (200, 400)
dimensions_2 = 200, 400, 600, 200
tuple_2 = tuple(cars_sorted)  # Create a tuple from a list
tuple_3 = tuple('A tuple!')  # Create a tuple from a string(or any iterable)

print(len(tuple_2))  # Number of tuple's elements
print(dimensions_2.count(200))  # Count specific element's number in a tuple
print(dimensions_2[0])  # Get first element from the tuple

# Unpacking the tuple
tuple_4 = (100, 'a', 300, 'c')
a, b, c, d = tuple_4  # Number of variables has to match tuple length

# Mutable elements inside a tuple
mutable_tuple = (1, [1, 2], {0: 'zero', 1: 'one'})
mutable_tuple[1].append(3)

# FOR LOOP

for car in cars_reverse_sorted:
    print(car)

for value in range(1, 5):
    print(value)
