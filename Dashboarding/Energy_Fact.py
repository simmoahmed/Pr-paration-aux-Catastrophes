import pandas as pd
import random

# Set the number of rows you want
num_rows = 100

# Generate random data
data = {
    'Geography_Key': [random.randint(1, 26) for _ in range(num_rows)],
    'Time_Key': [random.randint(1, 96) for _ in range(num_rows)],
    'Diesel_Reserve': [random.randint(100, 1000) for _ in range(num_rows)],
    'Gasoline_Reserve': [random.randint(100, 1000) for _ in range(num_rows)],
    'Electricity_Reserve': [random.randint(100, 1000) for _ in range(num_rows)],
    'Natural_Gas_Reserve': [random.randint(100, 1000) for _ in range(num_rows)],
    'KEROSENE_Reserve': [random.randint(100, 1000) for _ in range(num_rows)],
    'Diesel': [random.randint(100, 1000) for _ in range(num_rows)],
    'Gasoline': [random.randint(100, 1000) for _ in range(num_rows)],
    'Electricity': [random.randint(100, 1000) for _ in range(num_rows)],
    'Natural_Gas': [random.randint(100, 1000) for _ in range(num_rows)],
    'KEROSENE': [random.randint(100, 1000) for _ in range(num_rows)],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('Energy_Facts.csv', index=False)