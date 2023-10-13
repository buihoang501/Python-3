import timeit
import time


def func_one(n):
    return [str(num) for num in range(n)]


print(func_one(10))


def func_two(n):
    return list(map(str, range(n)))


print(func_two(10))

# current time
start_time = time.time()
# result run code
result = func_one(1000000)
# End time
end_time = time.time()

# Elapsed time
elapsed_time = end_time-start_time
print(elapsed_time)


# current time
start_time2 = time.time()
# result run code
result = func_two(1000000)
# End time
end_time2 = time.time()

# Elapsed time
elapsed_time2 = end_time2-start_time2
print(elapsed_time2)


# stmt argument - using mutiple line string for func/ for loops
stmt = '''   
func_one(100)
'''


# define func
setup = '''   
def func_one(n):
    return [str(num) for num in range(n)]
'''

# number is the times of running function
elapsed_time3 = timeit.timeit(stmt, setup, number=100000)
print(elapsed_time3)
# Total time of running 100000 times


# stmt2
stmt2 = '''
func_two(100)
'''

# setup2
setup2 = '''
def func_two(n):
    return list(map(str, range(n)))
'''
elapsed_time4 = timeit.timeit(stmt2, setup2, number=100000)
print(elapsed_time4)


stmt3 = '''
func_three(100000)
'''

setup3 = '''
def func_three(n):
    for item in n:
        yield item
'''
elapsed_time5 = timeit.timeit(stmt3, setup3, number=1000)
print(elapsed_time5)
