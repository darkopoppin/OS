import os
import sys
import subprocess

def cd(directory):
    os.chdir(directory)

def clr():
    subprocess.call("clear")

def dir():#Prints the current
   dirs = os.listdir()
   for dir in dirs:
       print(dir)

def environ():
    map = os.environ
    for key in map:
        print("{} - {}".format(key,map[key]))

def pwd():#Returns the current directory formatted as a prompt 
    return(os.getcwd() + "> ")

def program(name): #Launches the program by creating a subprocess
    subprocess.call(name) 
