import math
import statistics
from matplotlib import pyplot as plt


def deviation_mean(values):
    results = []
    avg = statistics.mean(values)
    for value in values:
        results.append(value - avg)
    return results


def standard_deviation(values):
    return math.sqrt(variance(values))


def variance(values):
    squared_deviations = []
    for d in deviation_mean(values):
        squared_deviations.append(d * d)
    return statistics.mean(squared_deviations)


def covariance(a, b):
    n = len(a)
    a = deviation_mean(a)
    b = deviation_mean(b)
    total = 0
    for i in range(n):
        total += a[i] * b[i]
    return total / (n - 1)


def correlation(a, b):
    col_1 = sum(multiply_lists(deviation_mean(a), deviation_mean(b)))
    col_2 = sum(square_list(deviation_mean(a)))
    col_3 = sum(square_list(deviation_mean(b)))
    return col_1 / math.sqrt(col_2 * col_3)


def multiply_lists(a, b):
    return [a * b for a, b in zip(a, b)]


def square_list(values):
    return [i ** 2 for i in values]


temperature = [14.2, 16.4, 11.9, 15.2, 18.5, 22.1, 19.4, 25.1, 23.4, 18.1, 22.6, 17.2]
sales = [215, 325, 185, 332, 406, 522, 412, 614, 544, 421, 445, 408]

plt.scatter(temperature, sales)

plt.xlabel('Temperature')
plt.ylabel('Sales')
plt.title('Correlation ' + str(correlation(temperature, sales)))
plt.show()
