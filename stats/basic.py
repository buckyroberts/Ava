from collections import Counter
from matplotlib import pyplot as plt


def mean(values):
    return sum(values) / len(values)


def median(values):
    num = len(values)
    sorted_values = sorted(values)
    middle = num // 2
    if num % 2 == 1:
        return sorted_values[middle]
    else:
        return (sorted_values[middle-1] + sorted_values[middle]) / 2


wings_eaten = [7, 21, 13, 16, 14, 20, 13, 16, 18, 14,
               8, 14, 12, 12, 16, 15, 16, 9, 15, 7]

wing_counts = Counter(wings_eaten)

x = []
y = []

for key in wing_counts.keys():
    x.append(key)
    y.append(wing_counts[key])

print('Contestants: ' + str(len(wings_eaten)))
print('Best: ' + str(max(wings_eaten)))
print('Worst: ' + str(min(wings_eaten)))
print('Average: ' + str(mean(wings_eaten)))
print('Median: ' + str(median(wings_eaten)))

plt.bar(x, y)
plt.axis([0, 25, 0, 5])
plt.xlabel('Wings eaten')
plt.ylabel('Number of contestants')
plt.title('Chicken Wings Contest Results')
plt.show()
