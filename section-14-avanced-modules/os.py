import os
import shutil
import send2trash
f = open('text.txt', mode='w+')
f.write('This is my string')
f.close()
# But I cann't specify the location of this file ?


print(os.getcwd())  # print current working directory

# list items in directories
print(os.listdir())
print(os.listdir('C:\WorkSpace'))


# moving files
# shutil.move(
#     'text.txt', 'C:\WorkSpace\Company\\training\code\python\section-14-avanced-modules')


# deleting filedeted.txt  in  \\code\\python
# send2trash.send2trash('filedeleted.txt')
filepath = 'C:\WorkSpace\Company\\training\code\python'

for folder, sub_folders, files in os.walk(filepath):
    print(folder)
    print(sub_folders)
    print(files)
