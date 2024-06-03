import pandas as pd
import random

# Set the number of rows you want
num_rows = 100

# Generate random data
data = {
    'Geography_Key': [random.randint(1, 26) for _ in range(num_rows)],
    'Time_Key': [random.randint(1, 96) for _ in range(num_rows)],
    'DryGrains_Reserve': [random.randint(100, 1000) for _ in range(num_rows)],
    'Oils_Reserve': [random.randint(100, 1000) for _ in range(num_rows)],
    'Legumes_Reserve': [random.randint(100, 1000) for _ in range(num_rows)],
    'CannedGoods_Reserve': [random.randint(100, 1000) for _ in range(num_rows)],
    'Flour_Reserve': [random.randint(100, 1000) for _ in range(num_rows)],
    'Dry_Grains': [random.randint(100, 1000) for _ in range(num_rows)],
    'Oils': [random.randint(100, 1000) for _ in range(num_rows)],
    'Legumes': [random.randint(100, 1000) for _ in range(num_rows)],
    'CannedGoods': [random.randint(100, 1000) for _ in range(num_rows)],
    'Flour': [random.randint(100, 1000) for _ in range(num_rows)],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('Supply_Facts.csv', index=False)