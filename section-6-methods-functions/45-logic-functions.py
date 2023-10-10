def check_even(number):
    return number % 2 == 0


check_number_1 = check_even(1)
check_number_2 = check_even(2)
print(check_number_1)
print(check_number_2)


def check_even_list(number_list):
    for num in number_list:
        if (num % 2 == 0):
            return True
        else:
            pass
    return False


is_even_1 = check_even_list([1, 3, 5])
is_even_2 = check_even_list([2, 3, 5])
print(is_even_1)
print(is_even_2)


def check_even_list2(number_list):
    even_list = []
    for num in number_list:
        if (num % 2 == 0):
            even_list.append(num)
        else:
            pass
    return even_list


even_list = check_even_list2([1, 2, 3, 4, 5, 6, 7, 8])
print(even_list)
