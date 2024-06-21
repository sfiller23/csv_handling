import pandas as pd
import os

# Get the current working directory
current_directory = os.getcwd()

def remove_empty_rows(input_csv_path, output_csv_path):
    # Load the CSV file
    data = pd.read_csv(input_csv_path)
    
    # Remove rows with any empty values
    cleaned_data = data.dropna()

    # Save the modified data to a new CSV file
    cleaned_data.to_csv(output_csv_path, index=False)

    print(f"Cleaned data saved to {output_csv_path}")



# Example usage
input_csv_path = os.path.join(current_directory, 'filtered_real_estate_data_Turkey.csv') 


output_csv_path = 'clean.csv'  # Update this path

# Ensure the output directory exists
#os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)

remove_empty_rows(input_csv_path, output_csv_path)