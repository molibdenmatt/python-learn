class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas(self, litres):
        print(f'Added {litres} litres of gasoline')


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas(self):  # Override the superclass method fill_gas
        print('Electric car doesn\'t need the gasoline!')


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'This car has {self.battery_size} kWh battery.')

    def get_range(self):
        if self.battery_size == 70:
            car_range = 240
        elif self.battery_size == 85:
            car_range = 270
        else:
            car_range = 0
        message = f'Your car_range is about {car_range} kilometers if battery is fully charged'
        print(message)