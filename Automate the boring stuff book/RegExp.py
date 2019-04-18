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