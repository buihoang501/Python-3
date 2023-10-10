mylist = [1, 2, 4, 5]
for item in mylist:
    print(item)
mystring = 'Hello Developers'
for _ in mystring:
    print('Hello')

sum = 0
for item in mylist:
    sum = sum + item
print(sum)

for item in mylist:
    if (item % 2 == 0):
        print('Divided by 2')
    else:
        print('Remainder')
mytuple = (1, 2, 3, 4, 5)
for item in mytuple:
    print(item)
mytuplelist = [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
for a, b, c in mytuplelist:
    print('tuple value {value}'.format(value=b))
mydict = {'name': 'Hoang', 'age': 25}
for key in mydict:
    print(key)
for item in mydict.items():
    print(item)
for key, value in mydict.items():
    print(value)
for value in mydict.values():
    print(value)
