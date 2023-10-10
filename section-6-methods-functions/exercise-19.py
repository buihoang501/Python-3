def myfunc(string):
    mystr = ''
    for index, value in enumerate(string):
        if (index % 2 == 0):
            mystr += value.upper()
        else:
            mystr += value.lower()
    return mystr
