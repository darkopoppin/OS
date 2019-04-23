import os
import sys
import subprocess
import getpass
from helpers import printf, redirection

def cd(directory):
    try:
        os.chdir(directory)
    except FileNotFoundError:
        if not directory: #if an argument is not present print current directory
            print("Current directory: " + os.getcwd())
        else:
            print("No such file or directory - " + directory)

def clr():
    subprocess.call("clear")

def dir(args):
    args = args.split()
    dirs = os.listdir(args[0])
    args.pop(0) #removes the requested directory from args so it can check in the next line for output redirection
    if args: # if there is requested output redirection
        args, PIPE = redirection(args) #opens a file for writing and returns it. Args here are not required but later in "def program" are and I wanted to use only one function for opening a file.
        for line in dirs:
            PIPE.write(line + "\n")
        PIPE.close()
        return

    if len(dirs) > 6: #if there are more than 6 files or directories -> format them in 3 columns
        printf(sorted(dirs,key=str, reverse = 0)) #prints the directories and files formatted
    else: #less than or = 6 print them on one line
        result = ""
        for i in range(0, len(dirs)):
            result += dirs[i] + "  "
        print(result)

def environ(args):
    environ_map = os.environ
    if args: # if there is redirection
        args = args.split()
        args, PIPE = redirection(args) #redirection opens a file for writing and returns it. Args here are not required but later in "def program" are and I wanted to use only one function for opening a file.
        for key in environ_map:
            PIPE.write(key + '-' + environ_map[key] + "\n")
        PIPE.close()
        return

    for key in environ_map:
        print("{} - {}".format(key,environ_map[key]))

def pwd(): #Returns the current directory formatted as a prompt 
    return(os.getcwd() + "> ")

def program(args):
    args = args.split()
    try:
        if args[-1] == '&': #run the program in the background
            args.remove('&')
            args, PIPE = redirection(args) #here PIPE receives the opened file for writing if redirection is necessary otherwise receives None 
            subprocess.Popen(args, stdout = PIPE)
 
        else:   #run it normally 
            args, PIPE = redirection(args)
            subprocess.run(args, stdout = PIPE)

        PIPE.close() #if a file is opened, close it 
            
    except FileNotFoundError:
        print("No such program or command")

    except AttributeError: #if there is no opened file closing a None type in line 62 will rise this error
        pass

def echo(args):
    args = args.split()
    text = ' '.join(args[0:-2]) #if there is redirection, slice and join only the comment to be displayed
    if args: # if there is redirection
        args, PIPE = redirection(args) #redirection opens a file for writing and returns it. Args here are not required but later in "def program" are and I wanted to use only one function for opening a file.
        PIPE.write(text + "\n")
        PIPE.close()
        return
    print(text)

def pause():
    getpass.getpass("Press Enter to continue.") #using getpass only to hide the input since its not necasssary to be shown and personally I prefer it this way

def exit():
    sys.exit()
