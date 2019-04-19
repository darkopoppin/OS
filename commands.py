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
    #print(len(dirs))
    columns = math.ceil(len(dirs)/3)
    #print("columns " + str(columns))
    fcolumn = dirs[0:columns]
    #print("fcolumn " + str(fcolumn))
    max_f = get_max_len(fcolumn)
    #print(max_f)
    scolumn = dirs[columns:columns*2]
    #print("scolumn " + str(scolumn))
    max_s = get_max_len(scolumn)
    tcolumn = dirs[columns*2:]
    #print("tcolumn" + str(tcolumn))

    while len(fcolumn) != 0:
        if len(fcolumn) == 1 and len(scolumn) == 0 and len(tcolumn) == 0:
            print(fcolumn.pop(0))
        elif len(fcolumn) >= 1 and len(scolumn) >= 1 and len(tcolumn) == 0:
            first = fcolumn.pop(0)
            second = scolumn.pop(0)
            print("{!s} {!s}".format(first + " "*(max_f - len(first)+1), second))
        else:
            first = fcolumn.pop(0)
            second = scolumn.pop(0)
            third = tcolumn.pop(0)
            print("{!s} {!s} {!s}".format(first + " "*(max_f-len(first)+4), second + " "*(max_s-len(second)+4), third))
        length = len(dirs)

def get_max_len(column):
    return len(max(column, key=len))
