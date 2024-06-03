import random

# Expanded example data for Geography_Dim table (Regions, Provinces, Municipalities in Morocco)
# Adding more entries to the existing list
expanded_morocco_data = [
    {"Region": "Tanger-Tétouan-Al Hoceima", "Province": "Tanger-Tétouan-Al Hoceima", "Municipality": "Tanger", "Latitude": 35.7781, "Longitude": -5.8135},
    {"Region": "Tanger-Tétouan-Al Hoceima", "Province": "Tanger-Tétouan-Al Hoceima", "Municipality": "Tetouan", "Latitude": 35.5668, "Longitude": -5.3684},
    {"Region": "Tanger-Tétouan-Al Hoceima", "Province": "Tanger-Tétouan-Al Hoceima", "Municipality": "Al Hoceima", "Latitude": 35.2452, "Longitude": -3.9364},
    {"Region": "L'Oriental", "Province": "L'Oriental", "Municipality": "Fès", "Latitude": 34.0339, "Longitude": -5.0008},
    {"Region": "L'Oriental", "Province": "L'Oriental", "Municipality": "Meknès", "Latitude": 33.8938, "Longitude": -5.5475},
    {"Region": "L'Oriental", "Province": "L'Oriental", "Municipality": "Ifrane", "Latitude": 33.5296, "Longitude": -5.1130},
    {"Region": "Fès-Meknès", "Province": "Fès-Meknès", "Municipality": "Marrakech", "Latitude": 31.6295, "Longitude": -7.9811},
    {"Region": "Fès-Meknès", "Province": "Fès-Meknès", "Municipality": "Essaouira", "Latitude": 31.5085, "Longitude": -9.7595},
]

# Generating SQL insert statements for Geography_Dim
geography_dim_sql = '\n'.join(
    "INSERT INTO Geography_Dim (Geography_Key, Region, Province, Municipality, Latitude, Longitude, MunicipalityArea) VALUES ({}, '{}', '{}', '{}', {}, {}, {});".format(
        index + 1, 
        data["Region"], 
        data["Province"], 
        data["Municipality"], 
        data["Latitude"], 
        data["Longitude"], 
        random.randint(100, 1000)  # Random area in square kilometers
    ) for index, data in enumerate(expanded_morocco_data)
)

geography_dim_sql[:500]  # Displaying the first 500 characters of the SQL script for Geography_Dim

