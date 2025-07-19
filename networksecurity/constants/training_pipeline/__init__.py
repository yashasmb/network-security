import os 
import sys
import numpy as np
import pandas as pd

'''

defing comman constant variables for training pipeline 
'''
TARGET_COLUMN = "Result"
PIPELINE_NAME = "NetworkSecurity"
ARTIFACT_DIR = "Artifacts"
FILE_NAME = "phisingData.csv"

TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

'''
Data Ingestion related constants start with "DATA_INGESTION VAR NAME"
'''

DATA_INGESTION_COLLECTION_NAME :str ="NetworkData"
DATA_INGESTION_DATABASE_NAME :str = "YASHASMB"
DATA_INGESTION_DIR_NAME :str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR :str = "feature_store"
DATA_INGESTION_INGESTED_DIR :str = "ingestion"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO :float = 0.2