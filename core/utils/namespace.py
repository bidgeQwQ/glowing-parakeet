

class Namespace:
    namespace = {}

    def __setattr__(self, name, value):
        if isinstance(name, str) and name not in {"namespace", }:
            if not name.startswith('__') and not name.endswith('__'):
                self.namespace[name] = value
        return super().__setattr__(name, value)

    def __repr__(self):
        s = ""
        for name, value in self.namespace.items():
            if name.startswith('__') and not name.endswith('__'):
                continue
            s += (", " if s != "" else "") + f"{name}={value}"

        return f"{self.__class__.__name__}({s})"

    def __str__(self):
        return self.__repr__()


class Rectangle2D(Namespace):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
