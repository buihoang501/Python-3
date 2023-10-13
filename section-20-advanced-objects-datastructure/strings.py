s = 'hello hoang 2'

# capitialize first world of string
print(s.capitalize())

# lower string
print('CapiTalize'.lower())

# count  letter
print(s.count('l'))

# find letter
print(s.find('o'))

# adding letter before fist letter and after last letter with string length increasing at a length
print(s.center(15, 'z'))

# expand  \t  / expandstabs()
print('hello\thi')

hello_string = 'hello\thi'
print(hello_string.expandtabs())

# check string is alphanumeric
string = 'hello'
print(string.isalnum())

# check string is alphabet
print(string.isalpha())

# check string is lower
print(string.islower())


# check string has white space
print(string.isspace())

# check Title case string / chữ hoa kí tự đầu từng từ
print(string.istitle())

# check string is upepr case
print(string.isupper())

# check string is end with letter o
print(string.endswith('o'))

# check the last letter of string
print(string[-1])

# split string into list by  e , seperating by 'e' letter
print(string.split('e'))

# partition  search for string first matching and spliting to three elements of a tuple
print(string.partition('e'))
my_new_string = 'hahahahahahaahahaa'
# searching for first a =>  my_new_string[1] => h , a ,ha.....
print(my_new_string.partition('a'))
