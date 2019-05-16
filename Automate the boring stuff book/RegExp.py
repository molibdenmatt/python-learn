import re  #regular expressions

message = 'Call me at 509-132-554 or 660-682-112'
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d)')  #r to skip escape characters \d=digit
mo = phoneNumRegex.search(message)  #match object
if mo : print(mo.group(1))  #1st group as () in the pattern
else : print('no match for pattern')
print(phoneNumRegex.findall(message))  #List of all matches

batRegex = re.compile(r'\(Bat(man|mobile|copter|bat)\)')  #\( to escape group sign and search for the "("
mo = batRegex.search('(Batmobile) lost a wheele')
print(mo.group())
print(mo.group(1))

batRegex2 = re.compile(r'Bat(wo)?man')  #(wo) can appear zero or one time
mo = batRegex2.search('The Adventures of Batman')
print(mo.group())

batRegex2 = re.compile(r'Bat(wo)*man')  #(wo) can appear any zero or more times
mo = batRegex2.search('The Adventures of Batwowowowoman')
print(mo.group())


batRegex2 = re.compile(r'Bat(wo)+man')  #(wo) Must appear at least once
mo = batRegex2.search('The Adventures of Batwoman')
print(mo.group())

haRegex = re.compile(r'(ha){3}')  #(ha) Must appear exactly 3 times
mo = haRegex.search('hahaha')
print(mo.group())

haRegex = re.compile(r'(ha){3,5}')  #(ha) Must appear 3-5 times, it will print max 5 times even if string is longer
mo = haRegex.search('hahahahahahaha')
print(mo.group())

digitRegex = re.compile(r'(\d){3,5}')  #will find the longest possible match starting from left. Greedy match
mo = digitRegex.search('123456789')
print(mo.group())

digitRegex = re.compile(r'(\d){3,5}?')  #will find the smallest possible match starting from left. Nongreedy match
mo = digitRegex.search('123456789')
print(mo.group())

