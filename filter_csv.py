import os
import pandas as pd

# Get the current working directory
current_directory = os.getcwd()

# Path to your ChromeDriver in the current directory
file_path = os.path.join(current_directory, 'world_real_estate_data(147k).csv') 

data = pd.read_csv(file_path)

# Filter the data by column title "country" with value "Turkey"
filtered_data = data[data['country'] == 'Turkey']

# Save the filtered data to a new CSV file
filtered_file_path = 'filtered_real_estate_data_Turkey.csv'
filtered_data.to_csv(filtered_file_path, index=False)

print(f'Filtered data saved to {filtered_file_path}')