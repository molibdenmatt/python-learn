import random
import os
from pathlib import Path

class Dice():
    def roll(self):
        return random.randint(1,6),random.randint(1,6)


for i in range(3):
    print(random.randint(10,20))

members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)  # Randomly chose from list
print(leader)

score = Dice()
print(score.roll())

path = Path('ecommerce')
print(path.exists())

mypath = Path().absolute()  # Absolute path
print(mypath)

mypath2 = Path('.')  # Relative path

new_path = Path('emails')
new_path.mkdir()
new_path.rmdir()

for file in mypath.glob('*.py'):
    print(file)

for file in mypath2.glob('*.py'):
    print(file)