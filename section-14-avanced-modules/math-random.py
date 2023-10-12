import math
import random

# help(math)
value = 1.22
print(math.floor(value))
print(math.floor(2.56))
print(math.ceil(2.16))
print(round(2.4))
print(round(2.6))
print(math.pi)
print(math.e)
print(math.log(math.e))
print(math.log(100, 10))
print(math.sin(30))
print(math.degrees(math.pi/2))
print(math.radians(90))

print(random.randint(0, 100))

# random.seed(arbitary_value) keeping random value after it
# print(random.seed(20))
print(random.randint(0, 100))
print(random.randint(0, 100))

mylist = list(range(0, 20))
print(mylist)

# random từ mylist 10 phần tử có thể trùng
print(random.choices(population=mylist, k=10))


# random từ mylist 10 phần tử không trùng
print(random.sample(population=mylist, k=10))

print(random.shuffle(mylist))

print(random.uniform(a=10, b=100))  # random floating number point 10-> 100

print(random.gauss(mu=0, sigma=1))  # random from  gauss distribution
# check from numpy library
