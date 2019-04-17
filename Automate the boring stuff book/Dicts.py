import pprint


myCat = {'size':'fat', 'color':'orange', 'disposition':'loud'}
print(myCat['size'])  # Access trough key
if 'color' in myCat:
    print('Yay!')

print(myCat.keys())
print(myCat.values())
print(myCat.items())
print(myCat.get('color', 'No color in dict'))  #get value of the key or print no color if there is no key in dict

if 'age' not in myCat:
    myCat['age'] = '2'

print(myCat.items())

myCat.setdefault('weight','5kg')  #If there is no weight key, it will add it. If it exists, nothing will happen

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for char in message.lower():
    count.setdefault(char, 0)
    count[char] += 1

pprint.pprint(count)