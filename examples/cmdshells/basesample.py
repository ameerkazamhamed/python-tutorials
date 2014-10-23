from cmd import Cmd

class BaseShell(Cmd):
    prompt = 'base> '

    def do_baseish(self,arg):
        print("This is from the base shell")

class SubShell(BaseShell):
    prompt = 'sub> '
   
    def do_hello(self,arg):
        print('Hello cmd shell')

if __name__ == '__main__':
    SubShell().cmdloop()

