import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
resume = '''
Mateusz Swieton
mobile: 508-123-1444
home: 509-321-5566
address: Random street 66
'''
print(phoneRegex.findall(resume))

""" 
Character classes:
\d - numeric 
\D - NOT numeric
\w - word (letter, numeric or underscore)
\W - not a word
\s - space, tab or newline
\S - not a space
"""

lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids milking, 7 swans' \
         'a swimming,6 geese a laying' \
         '5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree'

xmasRegex = re.compile(r'\d+\s\w+')  # One or more digit, space, one or more words
print(xmasRegex.findall(lyrics))

vowelRegex = re.compile(r'[aoieuAOIEU]')  # Create your own character class
lettersRegex = re.compile(r'[a-fA-F]')  # Create your own char class using range
antiVowelRegex = re.compile(r'[^aoieuAOIEU]')  # Everything except the vowels - ^ sign negates
print(vowelRegex.findall('Robocop eats baby food.'))








