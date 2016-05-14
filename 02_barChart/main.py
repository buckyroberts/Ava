from matplotlib import pyplot as plt

people = ['Bucky', 'Cassy', 'Joby']
hot_dogs = [14, 9, 11]

# Bars have default with of 0.8 so adding 0.1 centers them
x_values = [i + 0.1 for i, _ in enumerate(people)]

# You need list of numbers for chart, not strings
plt.bar(x_values, hot_dogs)

# Names of people will be centered on x-axis
plt.xticks([i + 0.5 for i, _ in enumerate(people)], people)

plt.title('Hot Dog Eating Contest')
plt.show()
