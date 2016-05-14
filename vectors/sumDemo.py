from matplotlib import pyplot as plt
from vectors.vector import Vector


axes = plt.axes()

v1 = Vector(dx=1, dy=0.5)
v2 = Vector(dx=1.5, dy=3)
v3 = Vector(dx=1, dy=1)
v4 = Vector.sum([v1, v2, v3])

axes.arrow(v1.x, v1.y, v1.dx, v1.dy, ec='r', linestyle='dashdot')
axes.arrow(v2.x, v2.y, v2.dx, v2.dy, ec='g', linestyle='dashdot')
axes.arrow(v3.x, v3.y, v3.dx, v3.dy, ec='b', linestyle='dashdot')
axes.arrow(v4.x, v4.y, v4.dx, v4.dy, ec='k')

plt.axis([0, 6, 0, 6])
plt.title('Sum of Multiple Vectors')
plt.show()
