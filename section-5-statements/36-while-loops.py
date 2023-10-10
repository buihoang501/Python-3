sum = 0

while sum < 10:
    print(sum)
    sum += 1
else:
    print('Sum >=10')

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    pass
for number in numbers:
    if (number == 3):
        continue
    print(number)

for number in numbers:
    if (number == 2):
        break
    print(number)
