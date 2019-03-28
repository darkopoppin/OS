import os
import sys
import subprocess

def cd(directory):
    os.chdir(directory)

def clr():
    subprocess.call("clear")

def dir():
   dirs = os.listdir()
   for dir in dirs:
       print(dir)

def environ():
    map = os.environ
    for key in map:
        print("{} - {}".format(key,map[key]))

def pwd():
    return(os.getcwd() + "> ")

def program(name):
    subprocess.call(name)
