customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])
print(customer.get("Name", "Matt"))
"""
doesn't shout an error even if the key is missing in dict. Instead it returns defaul val"Matt"
"""

customer["birthday"] = "01.01.2001"  # Setting new key:value pair
print(customer["birthday"])

digits = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    0: "zero"
}
phone_number = input("Provide your phone number")
for digit in phone_number:
    print(digits[int(digit)], end= " ")
