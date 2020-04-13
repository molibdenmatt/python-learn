"""
DICTIONARY
Is mutable
Is unordered
Is iterable
"""

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'], alien_0['points'])

# adding a key:value pair to the dict
alien_0['x_position'] = 0
alien_0['y_position'] = 25

# changing the value
alien_0['color'] = 'blue'

# removing a key:value pair
del alien_0['points']

user_0 = {
    'username': 'jkowalski',
    'first': 'jan',
    'last': 'kowalski',
}
# iterate over key:value pairs
for key, value in user_0.items():
    print('\nKey: ' + key)
    print('Value: ' + value)

# iterate over keys
for key_1 in user_0.keys():
    print(key_1)

for key_2 in user_0:  # by default python iterates over keys
    print(key_2)
    print(user_0[key_2])

for value_1 in user_0.values():
    print(value_1)

for data in set(user_0.values()):  # Pack values from dict to set => Get a set of only unique values
    print(data)
