from collections import Counter
from matplotlib import pyplot as plt

grades = [83, 84, 91, 87, 70, 67, 23, 78, 86, 99]


# Floor division where decimal place is removed //
def decile(grade):
    return grade // 10 * 10


# {80: 4, 90: 2, 70: 2, 20: 1, 60: 1}
histogram = Counter(decile(grade) for grade in grades)

plt.bar([x - 4 for x in histogram.keys()],  # center bars by shifting left
        histogram.values(),  # height
        8)  # width of 8

# x-axis range, y-axis range
plt.axis([-5, 105, 0, 5])

plt.xticks([10 * i for i in range(11)])

plt.ylabel('Number of Students')
plt.title('Test Scores')
plt.show()
