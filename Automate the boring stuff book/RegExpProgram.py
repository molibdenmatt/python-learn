import re
import pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# Possible number format: 415-555-0000, 555-0000, (415) 555-0000, 555-000 ext 12345
(
((\d\d\d)|(\(\d\d\d\)))?   # area code (optional)
(\s|-)   # first separator
\d\d\d  # first 3 digits
-   # separator
\d\d\d\d   # last 4 digits
(((ext(\.)?\s)|x)     # extension
(\d{2,5}))?  # extension number part (optional)
)
''', re.VERBOSE)

emailRegex = re.compile(r'''
# some.+_thing@something.smth
[a-zA-Z0-9_.+]+  # name part
@                # @ symbol
[a-zA-Z0-9_.+]+  # domain part
''', re.VERBOSE)

# Get the text
text = pyperclip.paste()

# Extract email and phone
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
'\n'.join(extractedEmail)

print(results)



