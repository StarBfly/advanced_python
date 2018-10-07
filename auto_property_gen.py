class AutoPropertyGenerator(type):
    def __init__(cls, name, bases, d):
        type.__init__(cls, name, bases, d)
        accessors = {}
        methods_prefix = ["get_", "set_", "del_"]
        for k in d.keys():
            v = getattr(cls, k)
            print(v)
            for i in range(3):
                if k.startswith(methods_prefix[i]):
                    accessors.setdefault(k[4:], [None, None, None])[i] = v
        for name, (getter, setter, deleter) in accessors.items():
            setattr(cls, name, property(getter, setter, deleter, ""))


class Example(metaclass=AutoPropertyGenerator):
    def __init__(self):
        self._x = None

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return 'y'
