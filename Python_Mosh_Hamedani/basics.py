#  https://www.youtube.com/watch?v=_uQrJ0TkZlc&list=WL&index=20&t=11s
import math

print('This is an YT 6h course')
print('*' * 10)  # multiply
boolean_val = True or False  # Has to be Capital letter

# age = input('What is your age? ')
# print(age)
# print(len(age))
course = 'Python for Beginners'
print(course.replace('Beginners', 'Noobs!'))
print(course.find('for'))  # Index of first char of searched string
print(100 ** 2)
x = -2.6
y = 2.9
print(round(x))  # 2.5> round up
print(abs(x))  # absolute value
print(math.ceil(y))  # round up
print(math.floor(y))  # round down

is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
elif is_cold:
    print("It's a cold day, wear warm clothes")
else:
    print("It's fine")
print("Enjoy your day")
