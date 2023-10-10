def myfunc(*args):
    mylist = []
    for item in args:
        if (item % 2 == 0):
            mylist.append(item)
        else:
            pass
    return mylist
