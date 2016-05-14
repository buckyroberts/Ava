from matplotlib import pyplot as plt

ax = plt.axes()

# x, y, dx, dy
ax.arrow(2, 2, 4, 3, head_width=0.4, head_length=0.8)

plt.axis([0, 10, 0, 10])
plt.title('Simple Vector')
plt.show()
