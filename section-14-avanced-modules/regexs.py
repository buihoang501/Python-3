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
