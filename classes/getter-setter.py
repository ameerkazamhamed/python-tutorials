import random

class Pen():
    def __init__(self):
        self.color = 'black'
        self.width = 7

    def __str__(self):
        return str(self.__dict__)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,value):
        if value == 'random':
            self.color = self.random_color()
        else:
            self.color = value

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
