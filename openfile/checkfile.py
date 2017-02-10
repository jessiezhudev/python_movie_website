import urllib
def read_text():
    quotes = open("/Users/zhuyudian/Documents/deep_learning/python_udacity/break.py")
    contents_of_file = quotes.read()
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(txt):
     check_content = urllib.urlopen("http://www.wdyl.com/profanity?q=" + txt)
     output = check_content.read()
     print(output)
     check_content.close()
read_text()
