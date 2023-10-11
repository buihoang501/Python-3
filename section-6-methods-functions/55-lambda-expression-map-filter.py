def square(num):
    return num**2


nums = [1, 2, 3, 4, 5, 6]

for num in map(square, nums):
    print(num)

square_nums = list(map(square, nums))
print(square_nums)


def splicer(string):
    if len(string) % 2 == 0:
        return 'EVEN'
    else:
        return string[0]


list_name = ['Hoang', 'Minh', 'Josh']
splicer_list = list(map(splicer, list_name))
print(splicer_list)


def check_even(num):
    return num % 2 == 0


even_list = list(filter(check_even, nums))
print(even_list)

for even_num in filter(check_even, nums):
    print(even_num)


def square(num): return num**2


print(list(map(square, nums)))
print(list(map(lambda num: num**2, nums)))

print(list(filter(lambda num: num % 2 == 0, nums)))
