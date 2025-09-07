import pandas as pd
import numpy as np

# Create a series from a list
list_data = [10, 20, 30, 40]
series_from_list = pd.Series(list_data)
print("Series from list:\n", series_from_list)

# Create a series from a NumPy array
array_data = np.array([1, 2, 3, 4, 5])
series_from_array = pd.Series(array_data)
print("\nSeries from NumPy array:\n", series_from_array)

# Create a series from a dictionary
dict_data = {'a': 100, 'b': 200, 'c': 300}
series_from_dict = pd.Series(dict_data)
print("\nSeries from dictionary:\n", series_from_dict)
