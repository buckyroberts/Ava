from matplotlib import pyplot as plt

ax = plt.axes()

# x, y, dx, dy
ax.arrow(2, 2, 3, 0, ec='r')
ax.arrow(5, 2, 0, 4, ec='g')

plt.axis([0, 8, 0, 8])
plt.title('Multiple Vectors')
plt.show()
