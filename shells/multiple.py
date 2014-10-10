from cmd import Cmd

class Base(Cmd):
    prompt = 'base> '

    def do_one(self,arg):
        One().cmdloop()

    def do_two(self,arg):
        Two().cmdloop()

class One(Cmd):
    prompt = 'one> '

    def do_hello(self,arg):
        print('Hello from One')

    def do_exit(self,arg):
        return True

class Two(Cmd):
    prompt = 'two> '

    def do_hello(self,arg):
        print('Hello from two')

if __name__ == '__main__':
    Base().cmdloop()
