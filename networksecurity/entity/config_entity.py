from datetime import datetime
import os
from networksecurity.constants import training_pipeline 



print(f"Training Pipeline Name: {training_pipeline.PIPELINE_NAME}"
      f"\nArtifact Directory: {training_pipeline.ARTIFACT_DIR}"
      f"\nFile Name: {training_pipeline.FILE_NAME}"
      f"\nTarget Column: {training_pipeline.TARGET_COLUMN}"
      f"\nTrain File Name: {training_pipeline.TRAIN_FILE_NAME}"
      f"\nTest File Name: {training_pipeline.TEST_FILE_NAME}"
)


class TrainingPipelineConfig:
    def __init__(self, timestamp: str = None):
        """
        Initializes the training pipeline configuration with a timestamp.
        If no timestamp is provided, the current datetime is used.
        """
        if timestamp is None:
            timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        
        self.pipeline_name = training_pipeline.PIPELINE_NAME
        self.artifact_dir = training_pipeline.ARTIFACT_DIR
        self.artifacts_name = os.path.join(self.artifact_dir, timestamp)
        self.timestamp = timestamp  


class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_ingestion_dir:str=os.path.join(
            training_pipeline_config.artifact_dir,training_pipeline.DATA_INGESTION_DIR_NAME
        )
        self.feature_store_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, training_pipeline.FILE_NAME
            )
        self.training_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TRAIN_FILE_NAME
            )
        self.testing_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TEST_FILE_NAME
            )
        self.train_test_split_ratio: float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name: str = training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name: str = training_pipeline.DATA_INGESTION_DATABASE_NAME
