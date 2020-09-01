import re

#this fuction take in the list of urls and converts it it 
def toArray():
    lineList = [line.rstrip('\n') for line in open('user.txt', 'r')]
    return lineList

#this fuction will strip item by item of the list
def get_line(text):
    line = text.pop()
    return line

def strip_user(line):
    user = 0
    return user


text = toArray()
line = get_line(text)
print(line)