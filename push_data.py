import os 
import sys
import json
import pandas as pd
import numpy as np
import pymongo
import certifi
# from pymongo.mongo_client import MongoClient
from networksecurity.exception.exception import NetworksecurityException
from networksecurity.logging.logger import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(f"Connecting to MongoDB at {MONGO_DB_URL}")
ca = certifi.where()


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(f"Error inserting data: {e}")    
        
    def cv_to_json_converter(self, cv_file_path):
        try:
            # Read the CSV file
            df = pd.read_csv(cv_file_path)

            # Convert DataFrame to a list of dictionaries
            records = df.to_dict(orient='records')

            return records

        except Exception as e:
            raise Exception(f"Error converting CSV to JSON: {e}")

    def insert_data_to_mongodb(self, records, database, collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)

            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

        


if __name__ == '__main__':
    FILE_PATH = "Network_Data\phisingData.csv"
    DATABASE = "YASHASMB"
    COLLECTION = "NetworkData"

    network_obj = NetworkDataExtract()
    records = network_obj.cv_to_json_converter(cv_file_path=FILE_PATH)
    print(records)
    
    no_of_records = network_obj.insert_data_to_mongodb(records, DATABASE, COLLECTION)
    print(f"Number of records inserted: {no_of_records}")