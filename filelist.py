import os
from os import listdir
filenames = os.listdir("./prank")
# print filenames
saved_path = os.getcwd()
print saved_path
os.chdir(r"/Users/zhuyudian/Documents/deep_learning/python_udacity/prank")
for filename in filenames:
    os.rename(filename, filename.translate(None, "0123456789"))
