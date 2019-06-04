def greet_user(name):
    print(f'Hi there, {name}!')
    print('Welcome aboard')


print("Start")
greet_user('Bob')
print("Finish")

try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age can\'t be 0')
except ValueError:
    print('Invalid value')


