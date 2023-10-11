class Person():
    stutent = 'Yes a student'

    def __init__(self, name):
        self.name = name

    def hello_name(self, learning):
        print('Hello {} and learning: {}'.format(self.name, learning))


hoang = Person(name='Hoang')
print(type(hoang))
print(hoang.name)
print(hoang.stutent)
hoang.hello_name('Python')


class Circle():
    pi = 3.14

    def __init__(self, radius=5):
        self.radius = radius
        self.area = radius*radius*self.pi

    def circumference(self):
        return 2*self.pi*self.radius


circle = Circle()
print(circle.area)
print(circle.circumference())
