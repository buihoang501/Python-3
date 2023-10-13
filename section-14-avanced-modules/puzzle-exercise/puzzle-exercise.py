import shutil
import os
import re

dir_to_zip = os.chdir(
    'C:\\WorkSpace\\Company\\training\\code\\python\\section-14-avanced-modules\\puzzle-exercise')

shutil.unpack_archive('unzip_me_for_instructions.zip', dir_to_zip, 'zip')


with open('extracted_content/Instructions.txt') as f:
    content_file = f.read()
    print(content_file)

pattern = r'\d{3}-\d{3}-\d{4}'


def search(file, pattern=pattern):
    f = open(file, 'r')
    content = f.read()

    if re.search(pattern, content):
        return re.search(pattern, content)
    else:
        return ''


results = []
for folder, subfolders, files in os.walk(os.getcwd()+"\\extracted_content"):
    for f in files:
        full_path = folder + "\\" + f
        results.append(search(full_path))

for match in results:
    if match != '':
        print(match.group())
