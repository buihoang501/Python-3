from random import randint
from random import shuffle
for num in range(0, 10, 2):
    print(num)

mylist = list(range(0, 10, 2))
print(mylist)

index = 0
for letter in 'abcd':
    print('Index {}-letter {}'.format(index, letter))
    index += 1

index2 = 0
word = 'abcd'
for letter in word:
    print(word[index2])
    index2 += 1
for letter in enumerate(word):
    print(letter)
for index, letter in enumerate(word):
    print(index, letter)

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd']
list = zip(list1, list2)
print(list)
for item in zip(list1, list2):
    print(item)
for a, b in list:
    print(a)
    print(b)
    print('\n')

list3 = ['1T', '2T', '3T']
for a, b, c in zip(list1, list2, list3):
    print('{} {} {}'.format(a, b, c))

x = [1, 2, 3]
print(1 in x)
print(4 in x)
mydict = {'name': 'Hoang', 'age': 25}
print('name' in mydict)
print('Hoang' in mydict.values())
numbers = [1, 5, 7, 9]
maxnum = max(numbers)
print(maxnum)
print(min(numbers))
shufflenums = shuffle(numbers)
print(shufflenums)  # None because it doesn't return any value
print(numbers)
randomnum = randint(0, 100)
print(randomnum)
name = input('Enter your name: ')
print(name)
