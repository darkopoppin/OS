import cmd
from commands import *

class myShell(cmd.Cmd):
    intro = "SMD"
    prompt = pwd() 
    def do_cd(self, arg):
        cd(arg)
        self.prompt = pwd()
    
    def do_dir(self, arg):
        dir()
    
    def do_clr(self, arg):
        clr()

    def do_environ(self, arg):
        environ()

    def default(self, arg):#dasdsa
        program(arg)

    def emptyline(self):
        pass #If 'enter' key is pressed, dont do anything

def main():
    myShell().cmdloop()

if __name__ == "__main__":
    main()
