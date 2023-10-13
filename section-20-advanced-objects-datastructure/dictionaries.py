# dictionaries comprehension

# key x, value x**2, 5 loops => dict ={0:0,1:1, 2:4,3:9,4:16}
dict_1 = {x: x**2 for x in range(5)}
print(dict_1)

# Two tuples  ('key_one',0)('key_one',1)
my_zip = zip(['key_one', 'key_two'], range(2))
for zip_item in my_zip:
    print(zip_item)

# keys are 'key_one' and 'key_two'
dict_2 = {x: y**2 for x, y in zip(['key_one', 'key_two'], range(2))}
print(dict_2)

# iteritems() return tuples of key and item in a dictionary
d = {'k1': 1, 'k2': 2}
for i in d.items():
    print(i)

for value in d.values():
    print(value)

for key in d.keys():
    print(key)

# Removed in python 3dict.iteritems(), dict.iterkeys(), and dict.itervalues().

# Instead: use dict.items(), dict.keys(), and dict.values() respectively.
