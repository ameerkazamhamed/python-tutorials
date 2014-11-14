class MyClass():
    my_class_attr = 'blah'
    overriden = 'lovely'

    def __init__(self):
        self.overriden = 'mine now'
        self.another = 'ok'

if __name__ == '__main__':
    instance = MyClass()
    print(instance)
    print(instance.__dict__)
    print(MyClass.__dict__)
    print(instance.__class__.__dict__)
    print('has myclass_attr',hasattr(MyClass,'my_class_attr'))
    print('has myclass_attr',MyClass.my_class_attr)
    print('has myclass_attr',hasattr(instance,'my_class_attr'))
    print('has myclass_attr',instance.my_class_attr)
    print('has overriden',hasattr(MyClass,'overriden'))
    print('has overriden',MyClass.overriden)
    print('has overriden',hasattr(instance,'overriden'))
    print('has overriden',instance.overriden)
    print('has another',hasattr(MyClass,'another'))
    print('has another',MyClass.another)
    print('has another',hasattr(instance,'another'))
    print('has another',instance.another)

