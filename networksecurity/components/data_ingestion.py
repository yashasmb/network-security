import os
import sys
import numpy as np
import pandas as pd
from typing import List
import pymongo
from sklearn.model_selection import train_test_split



from networksecurity.exception.exception import NetworksecurityException 
from networksecurity.logging.logger import logging
from networksecurity.entity.artifact_entity import DataIngestionArtifact
from networksecurity.entity.config_entity import DataIngestionConfig

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            logging.info(f"{'>>' * 20} Data Ingestion log started. {'<<' * 20}")
            self.data_ingestion_config = data_ingestion_config
            # self.client = pymongo.MongoClient(MONGO_DB_URL)
            # self.database = self.client.get_database("network_security")
            # self.collection = self.database.get_collection("network_data")
        except Exception as e:
            raise NetworksecurityException(e, sys) from e
        
    def export_data_as_dataframe(self) :
        '''
        Export data from MongoDB collection to a Pandas DataFrame.'''
        try:
            logging.info("Exporting data as DataFrame")

            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            collection = self.mongo_client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))

            if "_id" in df.columns:
                df.drop(columns=["_id"], inplace=True)
            
            df.replace({"na": np.nan}, inplace=True)

            return df

        except Exception as e:
            raise NetworksecurityException(e, sys) from e
    
    def export_data_into_feature_store(self, dataframe: pd.DataFrame) :
        '''
        Export data from DataFrame to feature store.
        This method is a placeholder and should be implemented based on the feature store requirements.
        '''
        try:
            logging.info("Exporting data into feature store")
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            os.makedirs(os.path.dirname(feature_store_file_path), exist_ok=True)
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe

        except Exception as e:
            raise NetworksecurityException(e, sys) from e

    def split_data_as_train_test(self, dataframe: pd.DataFrame) -> List[pd.DataFrame]:
        '''
        Split the data into training and testing sets.
        '''
        try:
            logging.info("Splitting data into train and test sets")
            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio, random_state=42)
            logging.info(f"Train set shape: {train_set.shape}, Test set shape: {test_set.shape}")
            
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)
            logging.info(f"Saving train and test sets to {self.data_ingestion_config.training_file_path} and {self.data_ingestion_config.testing_file_path}")
            
            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False, header=True)
            logging.info("Data split and saved successfully")
            
        except Exception as e:
            raise NetworksecurityException(e, sys) from e


    def initialize_data_ingestion(self) -> List[str]:
        try:
            logging.info("Initializing data ingestion process - calling export_data_as_dataframe method")
            dataframe = self.export_data_as_dataframe()
            logging.info("Data exported successfully as DataFrame")

            dataframe = self.export_data_into_feature_store(dataframe)
            self.split_data_as_train_test(dataframe)
            logging.info("Data split into train and test sets successfully")
            dataingestionartifact = DataIngestionArtifact( 
                train_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.testing_file_path
            )
            logging.info(f"Data Ingestion Artifact: {dataingestionartifact}")
            return dataingestionartifact
        except Exception as e:
            raise NetworksecurityException(e, sys) from e
