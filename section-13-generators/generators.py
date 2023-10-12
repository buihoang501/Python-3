def create_square(n):
    result = []
    for x in range(n):
        result.append(x**2)
    return result


print(create_square(10))
# memory used by result list


def create_square2(n):
    for x in range(n):
        yield x**2


print(list(create_square2(10)))

for x in create_square2(10):
    print(x)


def gen_fib(n):
    a = 1
    b = 1
    for x in range(10):
        yield (a)
        a, b = b, b+a


print(list(gen_fib(10)))


gen_numbers = gen_fib(10)
print(next(gen_numbers))
print(next(gen_numbers))
print(next(gen_numbers))
print(next(gen_numbers))
print(next(gen_numbers))
print(next(gen_numbers))
print(next(gen_numbers))
print(next(gen_numbers))
print(next(gen_numbers))
print(next(gen_numbers))
# print(next(gen_numbers))

s = 'Hello World'

# print(next(s))

s_iter = iter(s)  # enable iteration
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
