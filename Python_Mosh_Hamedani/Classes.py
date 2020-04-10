#  Pascal naming: class name: EmailNoteSmth

import modules  # or from modules import *
from ecommerce.shipping import calc_shipping

calc_shipping()

modules.hello()

class Point:
    def __init__(self, x, y):  # Constructor
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(10, 20)  # Create new class instance/object
print(point1.x)
print(point1.y)
point1.draw()  # Call method


class Human:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


#  Inherits methods from Human class
class Person(Human):
    pass


class Stranger(Human):
    pass  # If there's no method, insert pass


Stranger_1 = Stranger("Matt")
Stranger_1.talk()

bob = Person("Bob Smith")
bob.talk()

