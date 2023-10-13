my_list = [1, 2, 3]

# add a element to list
my_list.append(5)
print(my_list)

my_list.append([4, 6])
print(my_list)

# => nested list

# avoiding nested list by using extend method
my_list2 = [1, 2, 3]
my_list2.extend([4, 5])

print(my_list2)

# check index of element
print(my_list2[4])

# insert an elemnt to location in list
my_list2.insert(2, 'inserted element')
print(my_list2)

# remove the last elemnt of list and return that element
last_my_list_2 = my_list2.pop()
print(last_my_list_2)
print(my_list2)

# remove the first element of list and return that element
first_my_list_2 = my_list2.pop(0)
print(first_my_list_2)
print(my_list2)

# remove the element with value, nothing returns
inserted_value = my_list2.remove('inserted element')
print(inserted_value)
print(my_list2)


# reversing a list with reverse method
my_list2.reverse()
print(my_list2)

# count element of list
# Not found => count =0
print(my_list2.count(5))
# found
print(my_list2.count(4))
