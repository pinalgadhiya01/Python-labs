import pandas as pd
import numpy as np

# Sample DataFrame with missing values
df = pd.DataFrame({
    'Age': [25, 30, np.nan, 40, np.nan]
})

print("Original DataFrame:")
print(df)

df['Age'] = df['Age'].fillna(df['Age'].mean())

print("\nDataFrame After Filling Missing Values:")
print(df)
