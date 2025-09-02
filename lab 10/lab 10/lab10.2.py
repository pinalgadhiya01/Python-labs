import matplotlib.pyplot as plt
# Data for first line
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
# Data for second line
y2 = [2, 3, 5, 7, 11]
# Plotting the first line
plt.plot(x, y1, label='Squares', color='blue')
# Plotting the second line
plt.plot(x, y2, label='Primes', color='green')
# Adding labels and title
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Multiple Lines on Same Plot")
# Showing legend
plt.legend()
plt.show()
