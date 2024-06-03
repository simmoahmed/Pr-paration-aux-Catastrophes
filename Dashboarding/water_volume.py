import pandas as pd
import random

# Set the number of rows you want
num_rows = 100

# Generate random data
data = {
    'Barrier_Key': [random.randint(1, 50) for _ in range(num_rows)],
    'Geography_Key': [random.randint(1, 26) for _ in range(num_rows)],
    'Time_Key': [random.randint(1, 96) for _ in range(num_rows)],
    'Water_Volume': [random.randint(100, 1000) for _ in range(num_rows)],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('Water_Storage_Facts.csv', index=False)