from cmd import Cmd

class MyShell(Cmd):
    prompt = '> '

    def do_hello(self,arg):
        '''Prints Hello'''
        print("Hello")

if __name__ == '__main__':
    MyShell().cmdloop()
