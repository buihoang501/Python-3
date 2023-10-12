from collections import Counter
from collections import defaultdict
from collections import namedtuple

my_list = [1, 1, 1, 1, 2, 3, 3, 2, 1, 3, 4, 3, 3, 2, 1, 2, 3, 2, 4, 3, 5]

# Print count each number of list
print(Counter(my_list))

my_string_list = ['a', 'a', 'b', 'b', 'd', 'e']
print(Counter(my_string_list))

letters = 'aaaasdsadasdsadsadsadcvxcxzc'
print(Counter(letters))
c = Counter(letters)
# Xuất hiện nhiều nhất
print(c.most_common(1))
# Xuất hiện nhiều thứ 3
print(c.most_common(3))
# => Common patterns  Counter Object

# default dictionary
d = {'a': 10}
print(d['a'])
# print(d['b'])

# if it don't have that key => value 0 for wrong key
my_dict = defaultdict(lambda: 0)
print(my_dict['wrong_key'])


Dog = namedtuple('Dog', ['age', 'breed', 'name'])  # Dog is name as Class Name
# age breed name as class attribute
sammy = Dog(age=5, breed='Husky', name='Sam')
print(type(sammy))
print(sammy)
print(sammy[0])
