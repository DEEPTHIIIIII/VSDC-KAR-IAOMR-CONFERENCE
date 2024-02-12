import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/VSDC')
db = client['VSDC']
collection = db['registrations']

# Query data from MongoDB
data_from_mongodb = list(collection.find({}))  # Retrieve all documents, adjust query as needed

# Convert MongoDB data to DataFrame
df = pd.DataFrame(data_from_mongodb)

# Export DataFrame to Excel
excel_file_path = 'mongodb_data.xlsx'
df.to_excel(excel_file_path, index=False)

print("Data exported to Excel successfully!")
