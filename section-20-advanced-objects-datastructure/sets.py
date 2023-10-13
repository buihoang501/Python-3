s = set()

# add element to a set
s.add(1)
s.add(2)
print(s)

# clear all elements of a set
s.clear()
print(s)  # empty set

s = {1, 2, 3, 4, 5}
# copy a set
copy_set = s.copy()
print(copy_set)

# add a new elements  to old set
s.add(6)

# => only  old set changed, the new set is still old set value
print(copy_set)
print(s)

# compare two set
print(s.difference(copy_set))


# update set one is equal to the difference in set one with set two
set_one = {1, 2, 3}
set_two = {1, 4, 6}
print(set_one)
# result set one is {2,3}

set_one.difference_update(set_two)
print(set_one)

# remove/discard a element of a set
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)

# nothing happens so no element of set is 10
my_set.discard(10)
print(my_set)

# intersection / the common between two sets
common_set_1 = {1, 2, 3}
common_set_2 = {2, 4, 6}
# result is {2}
print(common_set_1.intersection(common_set_2))

# update a set  is  the intersection of two sets
common_set_3 = {1, 5, 3}
common_set_4 = {2, 5, 3}

common_set_3.intersection_update(common_set_4)

# result is {3,5} = common_set_3
print(common_set_3)

# checking no common between two sets with isdisjoint

disjoint_set_1 = {1, 2, 3}
disjoint_set_2 = {2, 3, 4}
disjoint_set_3 = {4, 5}


# false so the common of set_2 and set_1 is {2,3}
print(disjoint_set_1.isdisjoint(disjoint_set_2))

# true so no common of set_1 an  set_3
print(disjoint_set_1.isdisjoint(disjoint_set_3))

# false so the common of set_2 and set_3 is {4}
print(disjoint_set_2.isdisjoint(disjoint_set_3))


# checking the subset/ child set / tập hợp con của tập hợp cha
subset_1 = {1, 2}
subset_2 = {1, 2, 3, 5, 7, 11}
# result is true so subset_1 is a child of subset_2
print(subset_1.issubset(subset_2))

# checking the superset / parent set / tập hợp cha của một tập con

# result is true so subset_2 is a parent of subset_1
print(subset_2.issuperset(subset_1))

# checking the summeric_difference (phần bù của hai tập hợp) A,B
summeric_1 = {1, 2, 4}
summeric_2 = {2, 4, 6}

# summeric_1  -  sumeric_2  = {1,6}
print(summeric_1.symmetric_difference(summeric_2))
print(summeric_2.symmetric_difference(summeric_1))

# union / combine two sets
union_set_1 = {1, 2, 3}
union_set_2 = {3, 4}

# result  = {1,2,3,4} so set has unique elements
print(union_set_1.union(union_set_2))

# updating one set = the union of two sets
update_set_1 = {1, 2, 3}
update_set_2 = {4, 5, 6}

update_set_1.update(update_set_2)
# result = {1,2,3,4,5,6}
print(update_set_1)
