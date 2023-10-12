import re
text = 'My phone phone'
print('phone' in text)

pattern = 'phone'
match = re.search(pattern, text)
print(match)

print(match.start())  # index start first match
print(match.end())  # index end first match


matches = re.findall(pattern, text)  # get all matches
print(matches)

for match in re.finditer(pattern, text):  # iterate match
    print(match)  # match is  Match Object
    print(match.span())
    print(type(match.span()))
    print(match.group())  # Return the string matched by the RE


my_text = 'My phone is 098-098-8291'

# phone = re.search(r'\d\d\d-\d\d\d-\d\d\d', my_text)
# 3 digits - 3 digits- 4 digits
phone = re.search(r'\d{3}-\d{3}-\d{4}', my_text)


print(phone)

print(phone.group())


# compile together regular expressions // kết hợp nhiều single pattern với nhau => a  group of pattern
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

results = re.search(phone_pattern, my_text)

print(results.group())


# Because of using compile pattern => Can get each one of group results
print(results.group(1))
print(results.group(2))
print(results.group(3))
