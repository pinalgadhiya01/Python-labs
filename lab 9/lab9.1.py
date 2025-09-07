import pandas as pd

s1 = pd.Series([5,13,25,9,20])
s2 = pd.Series([2,4,6,8,7])

# Addition
add = s1 + s2
print("Addition:\n", add)

# Subtraction
sub = s1 - s2
print("\nSubtraction:\n", sub)

# Multiplication
mul = s1 * s2
print("\nMultiplication:\n", mul)

# Division
div = s1 / s2
print("\nDivision:\n", div)
