from matplotlib import pyplot as plt


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

axes = plt.axes()

v1 = Vector(0, 0, 3, 0)
v2 = Vector(3, 0, 0, 4)
v3 = Vector.add(v1, v2)

axes.arrow(v1.x, v1.y, v1.dx, v1.dy, ec='r')
axes.arrow(v2.x, v2.y, v2.dx, v2.dy, ec='g')
axes.arrow(v3.x, v3.y, v3.dx, v3.dy, ec='b')

plt.axis([0, 5, 0, 5])
plt.title('Multiple Vectors')
plt.show()
