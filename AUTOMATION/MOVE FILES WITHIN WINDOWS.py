import shutil
import os


source_dir = '/Users/alvba/Desktop/source'
target_dir = '/Users/alvba/Desktop/destination'
target_dir2 = '/Users/alvba/Desktop/destination2'


file_names2 = os.listdir(target_dir2)
for f in file_names2:
    os.remove(os.path.join(target_dir2, f))


file_names = os.listdir(source_dir)
for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir2)


shutil.move("/Users/alvba/Desktop/source/GOPR0036.jpg", "/Users/alvba/Desktop/destination2")