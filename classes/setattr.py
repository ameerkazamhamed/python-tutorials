"""Example of the use of __setattr__ and when it makes sense over @property

Sometimes @property gets in the way -- especially if you want to keep
the actual simple value attribute named the way you want rather than
hiding it (as we did in the setter-getter.py example). One such example
would be if you have other methods in place to automatically serialize
your objects into JSON notation and want to automatically exclude all
the private attributes in the __dict__ that begin with _.

In these cases the special __setattr__ method can be a better pick. This
special method intecepts *every* attribute definition so don't bog it down
with a lot of logic. It can also cause very hard to find bugs. But in the
right situation, such as below, it can be added without affecting other
logic and your class structure.

"""

import random

class Pen():
    def __init__(self):
        self.color = 'black'
        self.width = 7

    def __str__(self):
        return str(self.__dict__)

    def __setattr__(self,name,value):
        if name == 'color':
            if value == 'random':
                value = self.random_color()
        super().__setattr__(name,value)     # never forget to do this

    @staticmethod
    def random_color():
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return '#{:02x}{:02x}{:02x}'.format(r,g,b)


if __name__ == '__main__':
    pen = Pen()
    print(pen)
    pen.color = 'blue'
    print(pen)
    pen.color = 'random'
    print(pen)
