# Global
name = 'Global name'


def greet():
    # Enclosing
    name = 'Hoang'

    def hello():
        # Local
        print('Hello'+' ' + name)
    hello()


greet()

help(len)

x = 20


def myfunc():
    global x
    print(x)
    x = 30
    return x


myfunc()
print(x)
x = myfunc()
print(x)
