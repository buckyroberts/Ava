

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


def de_mean(values):
    results = []
    avg = mean(values)
    for v in values:
        results.append(v - avg)
    return results


wings_eaten = [3, 4, 5]
print(de_mean(wings_eaten))
