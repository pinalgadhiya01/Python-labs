import pandas as pd

s1 = pd.Series([7,8,9])
s2 = pd.Series([4, 5, 6])

vertical_stack = pd.concat([s1, s2], ignore_index=True)
print("Vertical Stack:\n", vertical_stack)

horizontal_stack = pd.concat([s1, s2], axis=1)
print("\nHorizontal Stack:\n", horizontal_stack)
