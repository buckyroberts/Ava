

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


def data_range(values):
    return max(values) - min(values)


def deviation_mean(values):
    results = []
    avg = mean(values)
    for value in values:
        results.append(value - avg)
    return results


def variance(values):
    squared_deviations = []
    for d in deviation_mean(values):
        squared_deviations.append(d*d)
    return mean(squared_deviations)


wings_eaten = [2, 4, 6]

print('Sample size: ' + str(len(wings_eaten)))
print('Average: ' + str(mean(wings_eaten)))
print('Variance: ' + str(variance(wings_eaten)))
