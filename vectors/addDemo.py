from matplotlib import pyplot as plt
from vectors.vector import Vector


axes = plt.axes()

v1 = Vector(0, 0, 3, 0)
v2 = Vector(3, 0, 0, 4)
v3 = Vector.add(v1, v2)

axes.arrow(v1.x, v1.y, v1.dx, v1.dy, ec='r')
axes.arrow(v2.x, v2.y, v2.dx, v2.dy, ec='g')
axes.arrow(v3.x, v3.y, v3.dx, v3.dy, ec='b')

plt.axis([0, 5, 0, 5])
plt.title('Adding Vectors')
plt.show()
