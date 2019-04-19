import os
import sys
import subprocess
from helpers import *

def cd(directory):
    try:
        os.chdir(directory)
    except FileNotFoundError:
        print("No such file or directory - " + directory)

def clr():
    subprocess.call("clear")

def dir():
    dirs = os.listdir()
    if len(dirs) > 6: #if there are more than 6 files or directories -> format them in 3 columns
        printf(sorted(dirs,key=str, reverse = 0)) #prints the directories and files formatted
    else: #less than or = 6 print them on one line
        result = ""
        for i in range(0, len(dirs)):
            result += dirs[i] + "  "
        print(result)
            

def environ():
    map = os.environ
    for key in map:
        print("{} - {}".format(key,map[key]))

def pwd():
    return(os.getcwd() + "> ")

def program(name):
    try:
        subprocess.Popen(name)
    except FileNotFoundError:
        print("No such program or command")

def echo(text):
    print(text)


#Helpers
