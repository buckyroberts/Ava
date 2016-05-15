import math


def mean(values):
    return sum(values) / len(values)


def median(values):
    num = len(values)
    sorted_values = sorted(values)
    middle = num // 2
    if num % 2 == 1:
        return sorted_values[middle]
    else:
        return (sorted_values[middle - 1] + sorted_values[middle]) / 2


def data_range(values):
    return max(values) - min(values)


def deviation_mean(values):
    results = []
    avg = mean(values)
    for value in values:
        results.append(value - avg)
    return results


def standard_deviation(values):
    return math.sqrt(variance(values))


def variance(values):
    squared_deviations = []
    for d in deviation_mean(values):
        squared_deviations.append(d * d)
    return mean(squared_deviations)


def covariance(a, b):
    n = len(a)
    a = deviation_mean(a)
    b = deviation_mean(b)
    total = 0
    for i in range(n):
        total += a[i] * b[i]
    return total / (n - 1)


x = [12, 30, 15, 24, 14, 18, 28, 26, 19, 27]
y = [20, 60, 27, 50, 21, 30, 61, 54, 32, 57]

print(covariance(x, y))
