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


# Additional Regex syntax
# matching dog or cat word
match_animal = re.search(r'dog|cat', 'This is my dog')

match_all_at = re.findall(
    r'.at', 'At the end of that book ! My love cat at that book is blue color! The cat with name is Doremon ')
# theo sau bởi một kí tự + at
print(match_animal.group())
print(match_all_at)

# Theo sau bởi 3 kí tự bao gồm cả whitespace +at
match_all_dt = re.findall(r'...at', 'the cat meeat kilat oopoat')

print(match_all_dt)

# start with a number

number_matches = re.findall(r'^\d', '3This is  1s 2s 2p 3s 3p 4s 3d 4p ')
print(number_matches)

# exclude [] ngoại trừ

my_string = 'There was 34  56a 2015 years'

# matching string with excluding digits at fisrt letter
string_matches = re.findall(r'[^\d]', my_string)
print(string_matches)

print(re.findall(r'[^!.?]+', my_string))


# Removing .  and ?
clean = re.findall(r'[^!.?]+', my_string)

print((' ').join(clean))


hyphen_text = 'My hyphen-text and hyphen-words'

# pattern_hyphen = r'[\w]+'
# pattern_hyphen = r'\w+-\w+'
pattern_hyphen = r'[\w]+-[\w]+'  # [] also combine together => inclusion


print(re.findall(pattern_hyphen, hyphen_text))


text1 = "Hello catfish"
text2 = "Hello catnap"
text3 = "Hello caterpillar"

# () parenthesis group together mutiple options
result_cat = re.search(r'cat(fish|nap|erpillar)', text1)
print(result_cat)
