import shutil
import zipfile
import os
f1 = open('text1.txt', 'w+')
f1.write('One file')
f1.close()

f2 = open('text2.txt', 'w+')
f2.write('Two file')
f2.close()


# Zip file
compress_file = zipfile.ZipFile('compress_file.zip', 'w')  # Creating zip file

# Zip text1.txt ,ZIP_DEFLATED => Zip one file
compress_file.write('text1.txt', compress_type=zipfile.ZIP_DEFLATED)
compress_file.write('text2.txt', compress_type=zipfile.ZIP_DEFLATED)

# Close compress_file
compress_file.close()


# Unzip file
zip_file_obj = zipfile.ZipFile('compress_file.zip', 'r')
# Unzipping all files, unzip folder (current working directory)
zip_file_obj.extractall('unzip')


# Zip with shutil
# os.chdir => change working directory to path
dir_to_zip = os.chdir(
    'C:\\WorkSpace\\Company\\training\\code\\python\\section-14-avanced-modules')


output_filename = 'example'

# creating zip file name is example  in dir_to_zip   with extend name .zip
# note cd zip folder before zip
# zipping all file all section-14-advanced-moduels
example_zip = shutil.make_archive(output_filename, 'zip', dir_to_zip)

print(example_zip)

# unziping with shutil

# Unzipping example.zip => into final_unzip folder ,  three argument zip is type of zip file
unzip_files = shutil.unpack_archive('example.zip', 'final_unzip', 'zip')
