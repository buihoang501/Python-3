def say_hello():
    print('Hello world!')


say_hello()


def say_hello_2(name='World'):
    print(f'Hello {name}')


say_hello_2()


def sum_two_numbers(a, b):
    return a+b


sum = sum_two_numbers(2, 3)
print(type(sum))
print(sum)

sum2 = sum_two_numbers('2', '3')
print(type(sum2))
print(sum2)
