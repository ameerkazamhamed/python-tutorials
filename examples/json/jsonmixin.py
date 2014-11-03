import json

class JSONMixin():

    def __str__(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls,string):
        json_ = json.loads(string) 
        instance = cls()
        instance.update(json_)
        return instance

    def update_from_json(self,json_):
        for key in json_: 
            if key in self.__dict__:
                self.__dict__[key] = json_[key] 

    update = update_from_json


# mixins look like inheritance in Python

class MyClass(JSONMixin):
    spam = True
    eggs = True

    def __init__(self):
        self.foo = 'bar'
        self.other = None

if __name__ == '__main__':
    mine = MyClass()
    print(mine)
    json_ = json.loads('{"other":1}') 
    mine.update(json_)
    print(mine)
    other = MyClass.from_json('{"other":5}')
    print(other)
