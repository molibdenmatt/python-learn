from car import Car, ElectricCar


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is sitting now.")

    def roll_over(self):
        print(self.name.title() + " is on it's back!")


my_new_car = Car('subaru', 'impreza', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.increment_odometer(5000)
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2018)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.fill_gas()


my_first_dog = Dog('Azor', 12)

print(f'My dog\'s name is {my_first_dog.name.title()}')
my_first_dog.sit()
my_first_dog.roll_over()
