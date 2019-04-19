import cmd
from commands import *

class myShell(cmd.Cmd):
    intro = "SMD"
    prompt = pwd() 
    def do_cd(self, arg):
        cd(arg)
        self.prompt = pwd()
    
    def do_dir(self, arg): #list the files and directories by calling dir()
        dir()              #from commands.py 
    
    def do_clr(self, arg): #clears the screen by calling clr() from commands.py
        clr()

    def do_environ(self, arg):
        environ()
    
    def do_echo(self, arg):
        echo(arg)

    def default(self, arg): #if none of the above commands is entered -> try invoking
        arg = arg.split()   #a program 
        program(arg)
    
    def emptyline(self): #when no command is entered - do nothing
        pass 
    
def main():
    myShell().cmdloop()

if __name__ == "__main__":
    main()
