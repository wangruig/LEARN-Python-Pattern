

class Singleton(object):
    _singleton = None

    def __new__(cls, *args, **kwargs):
        if cls._singleton is None:
            cls._singleton = object.__new__(cls, *args, **kwargs)
        return cls._singleton

s = Singleton()
print(s)
s1 = Singleton()
print(s1)