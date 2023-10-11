class IceCream():
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    # when call del method of Python will do this
    def __del__(self):
        print('Delete Instance Object')

    def __str__(self):
        return f'Icream costs {self.price}'
    # when call method len of python will do this

    def __len__(self):
        return self.quantity


my_icecream = IceCream(400, 5)

print(my_icecream)
print(len(my_icecream))
print(my_icecream.str())
del my_icecream
