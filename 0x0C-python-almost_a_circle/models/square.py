#!/usr/bin/python3
# Graham S. Paul (square.py)
"""
Assumed from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Explains class Square; assumed from class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Boots"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Achieves size"""
        return self.width

    @size.setter
    def size(self, value):
        """Calibrates size - calibrate width and height as size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Pulls [Square] (<id>) <x>/<y> - <size>"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.size)

    def update(self, *args, **kwargs):
        """
        If args: calibrates features in this order: id, width, height, x, y
        If no args given: calibrate features according to kwargs
        """
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.size = v
                elif k == 2:
                    self.x = v
                else:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Restores  dictionary constitution"""
        d = {}
        d["id"] = self.id
        d["size"] = self.size
        d["x"] = self.x
        d["y"] = self.y
        return d
