import matplotlib.pyplot as plt
# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
# Creating bar chart
plt.bar(languages, popularity, color='pink')
# Adding title and labels
plt.title("Popularity of Programming Languages")
plt.xlabel("Languages")
plt.ylabel("Popularity (%)")
# Displaying the chart
plt.show()
