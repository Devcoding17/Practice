# Pandas Basics
import pandas as pd

df = pd.DataFrame({
    'product': ['A', 'B', 'A'],
    'price': [100, 150, 200]
})

# Display the DataFrame
print(df)

print(df.groupby('product').mean())