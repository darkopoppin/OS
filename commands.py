import os
import sys
import subprocess
import math

def cd(directory):
    try:
        os.chdir(directory)
    except FileNotFoundError:
        print("No such file or directory - " + directory)

def clr():
    subprocess.call("clear")

def dir():
    dirs = os.listdir()
    if len(dirs) > 6:
        printf(sorted(dirs,key=str, reverse = 0))
    else:
        result = ""
        for i in range(0, len(dirs)):
            result += dirs[i] + " "
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

def printf(dirs):
    length = len(dirs)
    columns = math.ceil(len(dirs)/3)
    fcolumn = len(max(dirs[0:columns], key=len))
    print(dirs[0:columns])
    scolumn = len(max(dirs[columns:columns+3]))

    while length != 0:
        if length == 1:
            print(dirs.pop())
        elif length == 2:
            first = dirs.pop(0)
            second = dirs.pop(0)
            print("{!s} {!s}".format(first + " "*(fcolumn-len(first)+1), third))
        else:
            first = dirs.pop(0)
            second = dirs.pop(columns)
            third = dirs.pop(columns*2)
            print("{!s} {!s} {!s}".format(first + " "*(fcolumn-len(first)+1), second + " "*(scolumn-len(second)+1), third))
        length = len(dirs)
