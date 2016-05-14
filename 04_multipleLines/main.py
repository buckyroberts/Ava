from matplotlib import pyplot as plt

age = [1, 2, 3, 4, 5]
boys_iq = [14, 25, 63, 78, 139]
girls_iq = [10, 37, 42, 68, 154]

plt.plot(age, boys_iq, 'b-', label='Boys')
plt.plot(age, girls_iq, 'r:', label='Girls')

plt.legend(loc=9)
plt.title('Average IQ of Babies')
plt.show()
