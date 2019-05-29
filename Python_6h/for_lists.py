prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
print(f"Total: {total}$")

for x in range(4):
    for y in range(4):
        print(f'({x},{y})')

numbers = [5, 2, 5, 2, 2]
for i in numbers:
    for x in range(i):
        print('x', end='')
    print('')

numbers = [3, 6, 2, 8, 4 ,10, 2]
max = numbers[0]
for n in numbers:
    if n > max:
        max = n
print(max)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[1][1])
for row in matrix:
    for item in row:
        print(item)

numbers = [5,2,1,7,4]
numbers.append(13)
print(numbers)
numbers.insert(0, 11)
print(numbers)
numbers.remove(5)
numbers.sort()
numbers.reverse()

duplicates = [2,4,1,5,1,2,5,7,7,8,1]
for item in duplicates:
    if item in duplicates[(duplicates.index(item)):]:
        duplicates.remove(item) 
print(duplicates)

numbers = (1,2,3)  # tuple is immutable
x,y,z, = numbers  # Python unpacking
print(x, y, z)
