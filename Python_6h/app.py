import random

class Dice():
    def roll(self):
        return (random.randint(1,6),random.randint(1,6))

for i in range(3):
    print(random.randint(10,20))

members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)  # Randomly chose from list
print(leader)

score = Dice()
print(score.roll())
