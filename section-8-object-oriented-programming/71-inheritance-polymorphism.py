class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('{} says something'.format(self.name))


any_animal = Animal(name='Unkown')
any_animal.speak()


class Dog():
    def __init__(self, name):
        Animal.__init__(self, name)

    def speak(self, type):
        print('{} says {}'.format(self.name, type))


my_dog = Dog('Lucky')
my_dog.speak('Woof')
