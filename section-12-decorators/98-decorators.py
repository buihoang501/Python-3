def func():
    return 1


print(func)


def hello():
    print('Hello')


greet = hello
print(greet)

hello()
print(hello)

del hello
print(greet)
# hello is deleted but greet is still refereing to  old object in memory
# so call greet
greet()

# nested func


def hello(name='Hoang'):
    print('The hello func() has been executed')

    def greet():
        return '\t This is the greet() func inside hello!'
    print(greet())

    def welcome():
        return '\t This is welcome() insinde hello'
    print('This is the end of the hello function!')
    return welcome


welcome_hehe = hello()
print(welcome_hehe())


def cool():
    def super_cool():
        return 'Super Cool!'
    return super_cool


return_func = cool()
print(return_func())


# decorators
def hello_world():
    return 'hello world'


def other(some_func):
    print('Other code runs here!')
    print(some_func())


other(hello_world)


def new_decorator(original_func):
    def wrap_func():
        print('Some code, before the original func')
        original_func()
        print('Some code, after the original func')
    return wrap_func


# def fun_needs_decorator():
#     print('I want to be decorated!!')


# fun_needs_decorator()

# decorator_func = new_decorator(fun_needs_decorator)
# decorator_func()


@new_decorator
def fun_needs_decorator2():
    print('I want to be decorated 2!!')


fun_needs_decorator2()  # when calling this func will get context of new_decorator
# get fun_need_decorator2 into new_decorator and running context of new_decorator
