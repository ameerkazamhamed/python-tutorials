def bind(inst, func, as_=None):
    setattr(inst, as_ or func.__name__, func.__get__(inst, inst.__class__)) 

class MyClass():
    def __init__(self):
        self.foo = 'bar'

    def traditional_method(self):
        print('traditional method called')

if __name__ == '__main__':
    mine = MyClass()
    mine.traditional_method()

    def some_method(self):
        print('bound at runtime')

    bind(mine,some_method)
    mine.some_method()
    print(mine.some_method)

    bind(mine,some_method,'blah')
    mine.blah()
    print(mine.blah)
