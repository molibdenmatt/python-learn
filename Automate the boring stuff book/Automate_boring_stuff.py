# Automate Boring Stuff with Python - Udemy
# https://www.udemy.com/automate/learn/v4/t/lecture/3662882?start=0
import random, sys, os, math
import pyperclip

# test = 'yo ' + 'man' + '!' * 5
# print ('What is our name?')
# myName = input()
# print ('It is good to meet you, ' + myName)
# print ('The length of your name is:')
# print(len(myName))
# print('What is your age?')
# myAge = input()
# print ('You will be ' + str(int(myAge)+1) + ' in a year.')

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

# def hello(name):
#     global total #to make function use a global variable
#     total = 1
#     print('Hello ' + name)
#
# s = input("Your name?") # easy prompt
# print("Your name is: ", end="")
# print ('cat','dog', sep= '-and-')
# print(s)
# print("Hello, {}".format(s)) #another method to print
# x = 5/2.3
# print("{:.2f}".format(x)) #:.2f - format float, two digits after coma
#
# for i in range(65,65+26):
#     print("{} is {}".format(chr(i),i))
# for i in range(len(sys.argv)):
#     print(sys.argv[i]) #Will print every argument from command line e.g. python program.py arg1 arg2

def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError: #Can be just except, without specific error
        print('Error: you tried to divide by zero.')

print(div42by(2))
print(div42by(12))
print(div42by(0))

# Immutable types: ints, floats, strings, tuples



sys.exit() # end the script
print('You won\'t see me')



