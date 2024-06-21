import os
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

current_directory = os.getcwd()

# Path to your ChromeDriver in the current directory
firebase_config_path = os.path.join(current_directory, 'firebase.json')  # Ensure 'chromedriver' is in the current directory

real_estate_csv_path = os.path.join(current_directory, 'Turkish_Houses.csv') 
# Initialize Firebase Admin SDK
cred = credentials.Certificate(firebase_config_path)
firebase_admin.initialize_app(cred)
db = firestore.client()

# Read CSV file
df = pd.read_csv(real_estate_csv_path)

# Upload CSV data to Firestore with unique document IDs
collection_name = 'real-estate-info'
for _, row in df.iterrows():
    db.collection(collection_name).add(row.to_dict())

print('Data uploaded successfully')