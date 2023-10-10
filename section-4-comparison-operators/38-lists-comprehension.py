name = 'Hoang'
listname = []
for letter in name:
    listname.append(letter)
print(listname)

listname2 = [letter for letter in name]
print(listname2)

listname3 = [letter*2 for letter in name]
print(listname3)
numberlist = [num*3 for num in range(0, 5, 2)]
print(numberlist)
numberlist2 = [num**2 for num in range(0, 10) if num % 2 == 0]
print(numberlist2)
numbers = [1, 3, 4, 5, 8, 11, 32]
numberlist3 = [x if x % 2 == 0 else 'ODD' for x in numbers]
print(numberlist3)

numbers2 = [1, 2, 3, 4]
numbers3 = [2, 3, 4, 5]
results = []
for x in numbers2:
    for y in numbers3:
        results.append(y-x)
print(results)

results2 = [y-x for x in numbers2 for y in numbers3]
print(results2)
