import pandas as pd
import os
import random

# List of known Turkish city names with regular characters
known_cities = set([
    'Adana', 'Adiyaman', 'Afyonkarahisar', 'Agri', 'Aksaray', 'Amasya', 'Ankara', 'Antalya',
    'Ardahan', 'Artvin', 'Aydin', 'Balikesir', 'Bartin', 'Batman', 'Bayburt', 'Bilecik', 'Bingol',
    'Bitlis', 'Bolu', 'Burdur', 'Bursa', 'Canakkale', 'Cankiri', 'Corum', 'Denizli', 'Diyarbakir',
    'Duzce', 'Edirne', 'Elazig', 'Erzincan', 'Erzurum', 'Eskisehir', 'Gaziantep', 'Giresun', 'Gumushane',
    'Hakkari', 'Hatay', 'Igdir', 'Isparta', 'Istanbul', 'Izmir', 'Kahramanmaras', 'Karabuk', 'Karaman',
    'Kars', 'Kastamonu', 'Kayseri', 'Kirikkale', 'Kirklareli', 'Kirsehir', 'Kilis', 'Kocaeli', 'Konya',
    'Kutahya', 'Malatya', 'Manisa', 'Mardin', 'Mersin', 'Mugla', 'Mus', 'Nevsehir', 'Nigde', 'Ordu',
    'Osmaniye', 'Rize', 'Sakarya', 'Samsun', 'Sanliurfa', 'Siirt', 'Sinop', 'Sirnak', 'Sivas', 'Tekirdag',
    'Tokat', 'Trabzon', 'Tunceli', 'Usak', 'Van', 'Yalova', 'Yozgat', 'Zonguldak'
])

def extract_city_name(input_csv_path, output_csv_path):
    # Load the CSV file
    data = pd.read_csv(input_csv_path)
    
    # Function to extract the city name from the location string
    def get_city(location):
        for part in location.split(';'):
            part = part.strip()
            if part in known_cities:
                return part
        # If no known city is found, return a random city from known_cities
        return random.choice(list(known_cities))

    # Apply the function to the location column
    if 'location' in data.columns:
        data['location'] = data['location'].apply(get_city)
    else:
        print(f"No 'location' column found in {input_csv_path}")

    # Save the modified data to a new CSV file
    data.to_csv(output_csv_path, index=False)

    print(f"Modified data saved to {output_csv_path}")

# Example usage
input_csv_path = 'clean.csv'  # Update this path
output_csv_path = 'very_clean.csv'  # Update this path

# Ensure the output directory exists
#os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)

extract_city_name(input_csv_path, output_csv_path)