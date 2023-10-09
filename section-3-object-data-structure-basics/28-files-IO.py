with open('myfile.txt', mode='a+') as f:
    f.write('Creating a new file')
with open('myfile.txt', mode='r') as f:
    print(f.read())
with open('myfile.txt', mode='r') as f:
    print(f.read())

with open('myfile.txt', mode='a') as f:
    f.write('\nDo not be scare ')

myfile = open('myfile.txt')
contents = myfile.read()
print(contents)
myfile.close()
