import json

class Another():
    def __init__(self):
        self.some = 'thing'

class MyClass():
    spam = True
    eggs = True

    def __init__(self):
        self.foo = 'bar'
        self.other = None
        #self.another = Another()  # but this breaks it

    def __str__(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls,string):
        json_ = json.loads(string) 
        instance = cls()
        instance.update(json_)
        return instance

    def update(self,json_):
        for key in json_: 
            if key in self.__dict__:
                self.__dict__[key] = json_[key] 

if __name__ == '__main__':
    mine = MyClass()
    print(mine)
    json_ = json.loads('{"other":1}') 
    mine.update(json_)
    print(mine)
    other = MyClass.from_json('{"other":5}')
    print(other)
