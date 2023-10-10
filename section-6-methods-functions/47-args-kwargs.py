def sum_1(a, b):
    return sum((a, b))


print(sum_1(3, 2))


def sum_2(*args):
    print(args)
    return sum(args)


print(sum_2(2, 3, 4, 5, 6, 7, 8, 9))


def hello_name(**kwargs):
    print(kwargs)
    print('Hello {} {}'.format(kwargs['name'], kwargs['age']))


hello_name(name='Hoang', age=25)


def combine(*args, **kwargs):
    sum_money = sum(args)
    print('Hello {} {} Money:{}'.format(
        kwargs['name'], kwargs['age'], sum_money))


combine(1, 2, 3, 4, 5, 6, name='Hoang', age=25)
