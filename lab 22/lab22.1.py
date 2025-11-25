import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [30, 25, 35],
    'Salary': [50000.5, 45000, 60000],
    'Is_Employee': [True, True, False]
})

print(df.dtypes)
