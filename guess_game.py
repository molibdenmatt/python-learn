#This is a guess the number game
import random
print('Hi there! What is your name?')
name = input()

print('Well, ' + name + ' I\'m thinking of a number between 1 and 20')
secretNumber = random.randint(1, 20)
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your number is too low.')
    elif guess > secretNumber:
        print('Your number is too high.')
    else:
        break  # For the correct guess

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed in ' + str(guessesTaken) + ' trials!')
else:
    print('Nope. I was thinking of number ' + str(secretNumber))
