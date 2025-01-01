import os
from cassandra.cluster import Cluster
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
user_id = os.getenv("ASTRA_DB_USER_ID")
api_key = os.getenv("ASTRA_DB_API_KEY")
db_id = os.getenv("ASTRA_DB_DATABASE_ID")
region = os.getenv("ASTRA_DB_REGION")

print(f"User ID: {user_id}")
print(f"API Key: {api_key}")
print(f"Database ID: {db_id}")
print(f"Region: {region}")

# Optional: Test connectivity
cluster = Cluster(
    cloud={'secure_connect_bundle': '/path/to/secure_connect_bundle.zip'}
)
session = cluster.connect()
print("Connected to Astra DB successfully.")
