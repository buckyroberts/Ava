from matplotlib import pyplot as plt

age = [23, 14, 54, 34, 76, 12]
pullups = [12, 7, 8, 13, 2, 4]

plt.scatter(age, pullups)

plt.xlabel('Age')
plt.ylabel('Pullups')
plt.title('Age vs. Number of Pullups')
plt.show()
