

class Vector:

    def __init__(self, x=0, y=0, dx=0, dy=0):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def __str__(self):
        return str([self.x, self.y, self.dx, self.dy])

    @staticmethod
    def add(v1, v2):
        v = Vector(v1.x, v1.y)
        v.dx = v1.dx + v2.dx
        v.dy = v1.dy + v2.dy
        return v

    @staticmethod
    def sum(vectors):
        v = Vector(vectors[0].x, vectors[0].y)
        for vector in vectors:
            v.dx += vector.dx
            v.dy += vector.dy
        return v
