from collections import Counter
from matplotlib import pyplot as plt

wings_eaten = [7, 21, 13, 16, 14, 20, 13, 16, 18, 14,
               8, 14, 12, 12, 16, 15, 16, 9, 15, 7]
wing_counts = Counter(wings_eaten)

x = []
y = []

for key in wing_counts.keys():
    x.append(key)
    y.append(wing_counts[key])

plt.bar(x, y)

# Axis ranges
plt.axis([0, 25, 0, 5])

plt.xlabel('Wings eaten')
plt.ylabel('Number of contestants')
plt.title('Chicken Wings Contest Results')
plt.show()
