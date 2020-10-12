# ZeroDivisionError
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("Give me to numbers to divide")
print("Type 'q' to end the script")

while True:
    first_number = input("\nfirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Second number can't be zero")
    else:
        print(answer)

# FileNotFoundError
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print(f"Sorry, but {filename} was not found :(")

# Do nothing on error(pass)
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    pass
else:
    words = contents.split()
    num_words = len(words)