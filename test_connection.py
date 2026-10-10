import os
from pathlib import Path
from dotenv import load_dotenv
from pymongo import MongoClient

ENV_PATH = Path(__file__).resolve().parent / ".env"
load_dotenv(ENV_PATH, override=True)

uri = os.getenv("MONGO_DB_URL")

if not uri:
    raise ValueError("MONGO_DB_URL not loaded")

client = MongoClient(uri, serverSelectionTimeoutMS=10000)

try:
    client.admin.command("ping")

    print("Connected successfully")
    print("Cluster host:", client.address)
    print("Databases:", client.list_database_names())

    db = client["NetworkSecurity"]
    collection = db["NetworkData"]

    print("Collection count:", collection.count_documents({}))
    print("Collections:", db.list_collection_names())

finally:
    client.close()