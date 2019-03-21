# Automate Boring Stuff with Python - Udemy
# https://www.udemy.com/automate/learn/v4/t/lecture/3662882?start=0
# print("hello world")
#
import random, sys, os, math
import pyperclip



# test = 'yo ' + 'man' + '!' * 5
# print(test)
#
# print ('What is our name?')
# myName = input()
# print ('It is good to meet you, ' + myName)
# print ('The length of your name is:')
# print(len(myName))
# print('What is your age?')
# myAge = input()
# print ('You will be ' + str(int(myAge)+1) + ' in a year.')

# name = 'Pjoter'
# if name == 'Mati':
#     print('Hi Mati')
# elif name == 'Janusz':
#     print('Oj Janusz...')
# else:
#     print('Hi stranger')
# print('Done')
#
# bool('')   # returns Falsy value
#
# name = ''
# while name != 'your name':
#     print("type your name")
#     name = input()
# print('Thanks')

# name = ''
# while True:
#     print('type your name')
#     name = input()
#     if name == 'your name':
#         break

# spam = 0
# while spam < 5:
#     spam = spam + 1
#     if spam == 3:
#         continue #go back to while beginning
#     print('spam is ' + str(spam))

# total = 0
# for num in range(101):
#     total = total + num
# print(total)


# for i in range(12, 32, 2): #(from, to, step)
#     print
# print(random.randint(1,10))
# pyperclip.copy('Hello World copied')
# print(pyperclip.paste())

def hello(name):
    print('Hello ' + name)


hello('Alice')
hello('Bob ')

s = input("Your name?") # easy prompt
print("Your name is: ", end="")
print(s)
print("Hello, {}".format(s)) #another method to print
x = 5/2.3
print("{:.2f}".format(x)) #:.2f - format float, two digits after coma

for i in range(65,65+26):
    print("{} is {}".format(chr(i),i))



sys.exit() # end the script
print('You won\'t see me')
