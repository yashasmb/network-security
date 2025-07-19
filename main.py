from networksecurity.components.data_ingestion import DataIngestion 

import os
import sys
from networksecurity.exception.exception import NetworksecurityException
from networksecurity.logging.logger import logging
# from networksecurity.entity.artifact_entity import DataIngestionArtifact
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
if __name__ == "__main__":
    try:
        logging.info(f"{'>>' * 20} Network Security Project started. {'<<' * 20}")
        training_pipeline_config = TrainingPipelineConfig()
        logging.info(f"Training Pipeline Config: {training_pipeline_config}")
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        logging.info(f"Data Ingestion Config: {data_ingestion_config}")
        logging.info(f"initializing data ingestion...")
        data_ingestion_artifact = data_ingestion.initialize_data_ingestion()
        logging.info(f"Data Ingestion Artifact: {data_ingestion_artifact}")
        logging.info(f"{'>>' * 20} Network Security Project completed. {'<<' * 20}")
        
    except Exception as e:
        raise NetworksecurityException(e, sys) from e