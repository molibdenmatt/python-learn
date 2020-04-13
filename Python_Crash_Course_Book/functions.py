# positional arguments
def describe_pet(pet_name, pet_type='dog'):  # dog is a default value if none provided while calling function
    print(f'Your pet\'s name is {pet_name}, and it\'s a {pet_type}')


describe_pet('ginger', 'cat')

# key arguments - order doesn't matter
describe_pet(pet_name='john', pet_type='dog')
describe_pet('fluffy')  # will become a default - dog


# *args
def make_pizza(size, *toppings):
    print(f'Preparing a {size} pizza for you with:')
    for topping in toppings:
        print(topping)


make_pizza('large', 'onion', 'beef', 'mozzarella')


# **kwargs
def build_profile(first, last, **details):
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in details.items():
        profile[key] = value
    return profile


user_profile = build_profile('John', 'Kew', location='USA', hobby='drums')
print(user_profile)
