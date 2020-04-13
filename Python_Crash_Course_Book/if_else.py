car = 'bmw'
print(car == 'bmw')
age_0 = 22
age_1 = 28
print(age_0 >= 21 or age_1 <= 21)
print(age_0 == 22 and False)

requested_toppings = ['pieczarki', 'cebula', 'ser']

if 'salami' not in requested_toppings:
    print('I want salami!')
elif 'cebula' in requested_toppings:
    print('good pieczarki!')
else:
    print('All good')

requested_toppings = []

if requested_toppings:  # Check if list is not empty. Empty list = False, not empty = True
    for topping in requested_toppings:
        print(f'Adding {topping} to the pizza')
else:
    print('Do you really want an emtpy pizza?')

