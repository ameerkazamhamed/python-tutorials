

class MyClass():

    def __init__(self):
        self.spam = 'yum'
        self.eggs = 'poached'
        self._oven = 'hidden'

    @staticmethod
    def _no_underscore(d):
        return [key for key in d if not key.startswith('_')] 

    def public_attributes(self):
        return self._no_underscore(self.__dict__)

if __name__ in '__main__':
    my = MyClass()
    print(my.public_attributes())
