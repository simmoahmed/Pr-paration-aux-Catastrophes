import pandas as pd
from datetime import datetime, timedelta

# Generate data for Time_Dim table
start_date = datetime(2015, 1, 1)
end_date = datetime(2023, 12, 31)
delta = timedelta(days=1)

# Creating a list of dates
dates = pd.date_range(start_date, end_date, freq='D')

# Creating the DataFrame for Time_Dim
time_dim_data = pd.DataFrame({
    'Time_Key': range(1, len(dates) + 1),
    'FullDate': dates.date,
    'Month': dates.month,
    'MonthName': dates.strftime('%B'),
    'Quarter': dates.to_period('Q').strftime('Q%q'),
    'Year': dates.year
})

# Generate SQL insert statements for Time_Dim
time_dim_sql = '\n'.join(
    "INSERT INTO Time_Dim (Time_Key, FullDate, Month, MonthName, Quarter, Year) VALUES ({}, '{}', {}, '{}', '{}', {});".format(
        row.Time_Key, row.FullDate, row.Month, row.MonthName, row.Quarter, row.Year
    ) for index, row in time_dim_data.iterrows()
)

