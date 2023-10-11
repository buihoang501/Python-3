print(list)
print(type(set([1, 2, 2, 3])))


class Person():
    stutent = 'Yes a student'

    def __init__(self, name):
        self.name = name


hoang = Person(name='Hoang')
print(type(hoang))
print(hoang.name)
print(hoang.stutent)
