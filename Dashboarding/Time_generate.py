import csv
from datetime import datetime, timedelta

def get_quarter(month):
    if month <= 3:
        return 'Q1'
    elif month <= 6:
        return 'Q2'
    elif month <= 9:
        return 'Q3'
    else:
        return 'Q4'

def generate_time_data():
    data = []
    current_date = datetime(2017, 1, 1)

    for i in range(1, 1001):
        month = current_date.month
        quarter = get_quarter(month)

        row = {
            'Time_Key': i,
            'FullDate': current_date.strftime('%Y-%m-%d'),
            'Month': month,
            'MonthName': current_date.strftime('%B'),
            'Quarter': quarter,
            'Year': current_date.year
        }

        data.append(row)

        current_date += timedelta(days=30)  # Ajoute un mois approximatif

        # Limite les mois à chaque année jusqu'en 2024
        if current_date.year > 2024:
            break

    return data

# Générer les données
time_data = generate_time_data()

# Écrire les données dans un fichier CSV
csv_file_path = 'Time.csv'
fieldnames = time_data[0].keys()

with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(time_data)

print(f"Données générées avec succès et enregistrées dans {csv_file_path}")