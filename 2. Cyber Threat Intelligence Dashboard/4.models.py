from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client.cti_db

# Collections
threats_collection = db.threats  # Stores IOCs, threat levels, etc.
trends_collection = db.trends    # Stores historical data for visualizations
