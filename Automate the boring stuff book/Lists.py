import copy

# spam = [10, 20, 30]
# spam[1:3] = ['CAT', 'DOG', 'MOUSE']
# print(spam)
# print(spam[:2]) # from zero to 2 not including 2
# print(spam[1:]) # from 1st to the end
# del spam[2] # delete 2nd element
# print(spam)
#
# print("List length: " + str(len(spam)))
#
# print(list('Hello'))
# spam = spam + [1, 2, 3]
# spam = spam * 2
# print('CAT' in spam)
# print('4' not in spam)

spam = list(range(0,100,2))
print(spam)

supplies = ['pens', 'staplers', 'binders', 'lighters']
for i in range(len(supplies)):
    print (str(i) + ' Is index of ' + supplies[i] + ' in supplies')

cat = ['fat', 'orange', 'loud']
size, color, disposition = cat # multiple assignment

# size, color, disposition = 'small', 'black', 'shy' # multiple assignment in another way
# print(size)
# print(color)
# print(disposition)
# color, size = size, color # values SWAP

#LIST METHODS
# spam = ['hi', 'hello', 'howdy', 'heyah']
# print(spam.index('hello'))  # Index of first occurrence in the list
# spam.append('hey there')  # Add at the end of a list
# spam.insert(1, 'Hooah')  # Insert element at the index 1
# spam.remove('howdy')  # remove first occurrence
# print(spam)
# spam = [2, 5, 3.14, 1, -7]
# spam.sort()  # Sorting(also works with alphabet - can't mix numbers and strings)
# spam.sort(reverse=True)
# spam.sort(key=str.lower) # True alphabetical sort. Default one is based on ASCII
# print(spam)

#String is almost like a list
name = "Zophie"
print(name[0:3])

new_list = copy.deepcopy(spam)  # Creates a whole new copy of list, not just the reference
print('blahblahblah' + \
      'newlineblahblah')

#STRINGS
print('-'.join(['cat', 'bat', 'rat']))  #Join the list using - separator
rjust(),ljust,just("*")
strip(),lstrip(),rstrip("characters")


