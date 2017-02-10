import os
from os import listdir
import time
import webbrowser

filenames = os.listdir("./")
saved_path = os.getcwd()
print(filenames)
for filename in filenames:
    os.rename(filename, filename.translate(None, "0123456789"))
time.sleep(20)
webbrowser.open("http://music.163.com/#/mv?id=375527")
