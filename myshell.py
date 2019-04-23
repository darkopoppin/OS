import cmd, sys
from commands import *

class myShell(cmd.Cmd):

    def __init__(self, stdin = None):
        super().__init__()
        self.intro = "SMD"
        self.prompt = pwd()
        if stdin != None:
            with open (stdin, 'r') as f:
                commands = f.readlines()
                commands.append("exit")
                self.cmdqueue = commands

    def do_cd(self, arg):
        cd(arg)
        self.prompt = pwd()
    
    def do_dir(self, arg): #list the files and directories by calling dir()
        dir(arg)              #from commands.py 
    
    def do_clr(self, arg): #clears the screen by calling clr() from commands.py
        clr()

    def do_environ(self, arg):
        environ(arg)
    
    def do_echo(self, arg):
        echo(arg)
    
    def do_exit(self, arg):
        self.close()
    
    def do_pause(self, arg):
        pause()

    def do_exit(self, arg):
        exit()

    def default(self, arg): #if none of the above commands is entered -> invoke a program
        program(arg)

    def emptyline(self): #when no command is entered - do nothing
        pass 
    
def main():
    try:
        myShell(stdin=sys.argv[1]).cmdloop()

    except FileNotFoundError:
        print ("File not found! Running in normal mode.")
        myShell().cmdloop()

    except IndexError:
        myShell().cmdloop()


if __name__ == "__main__":
    main()
