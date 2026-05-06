class Point:
    _color = 0
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f"{self._x} {self._y}"

    def get_cords(self):
        return (self._x, self._y)
    
    def dist(self, other):
        cords = other.get_cords()
        return ((self._x - cords[0]) ** 2 + (self._y - cords[1]) ** 2) ** (1/2)

    def set_color(self, n):
        self._color = n

    def get_color(self):
        return self._color