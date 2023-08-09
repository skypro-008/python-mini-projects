import json

import pandas as pd

# Load data from json file
with open('sales_data.json', 'r') as f:
    data = json.load(f)

# Convert data to pandas DataFrame
df = pd.DataFrame(data)

# Convert date column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Group data by store and date
grouped = df.groupby(['store', 'date'])

# Compute mean sales per day for each store
results = grouped['sales'].mean()

# Print the results
print(results)
