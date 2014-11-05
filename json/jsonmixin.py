import json

class JSONMixin():
    """Simple JSON serialization with basic marshalling. Not intended for
    speed nor deep JSON operations.
    """

    @property
    def _json_attrs(self):
        """Used to identify attributes that can be used for json.
        By default any attribute not beginning with _ will be included.
        Override this mixed-in method to return a static dict referring
        to the attributes you want to include. By default this dictionary
        is created on every call with a comprehension filtering out
        anything in `self.__dict__` that starts with _.
        """

        d = self.__dict__
        return {key:d[key] for key in d if not key.startswith('_')}

    @_json_attrs.setter
    def _json_attrs(self,value):
        raise AttributeError('_json_attr is read-only')

    @_json_attrs.deleter
    def _json_attrs(self,value):
        raise AttributeError('_json_attr is read-only')

    def update_from_json(self,json_):
        """Called by `from_json*`. Override for more control."""
        attrs = self._json_attrs
        for key in json_: 
            if key in attrs:
                self.__dict__[key] = json_[key] 
        return self

    def to_json(self):
        """Override this if you need more control of the JSON generated."""
        return json.dumps(self._json_attrs)

    @classmethod
    def from_json(cls,json_):
        """An alternative constructor. Override `update_from_json` instead."""
        if type(json_) is str:
            json_ = json.loads(json_) 
        instance = cls()
        instance.update_from_json(json_)
        return instance

    @classmethod
    def from_json_file(cls,fname):
        """An alternative constructor. Override `update_from_json` instead."""
        with open(fname, 'r') as f:
            return cls.from_json(json.load(f))

    def __str__(self):
        """As a convenience but use explicit `to_json` instead usually."""
        return self.to_json()

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
    mine.update_from_json(json_)
    print(mine)
    other = MyClass.from_json('{"other":5}')
    print(other)
