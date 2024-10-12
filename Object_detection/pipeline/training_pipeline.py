import sys, os
from Object_detection.logger import logging
from Object_detection.exception import SignException
from Object_detection.components.data_ingestion import DataIngestion

from Object_detection.entity.config_entity import (DataIngestionConfig)
from Object_detection.entity.artifacts_entity import (DataIngestionArtifact)



class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()


    def start_data_ingestion(self)-> DataIngestionArtifact:
        try: 
            logging.info(
                "Entered the start_data_ingestion method of TrainPipeline class"
            )
            logging.info("Getting the data from URL")

            data_ingestion = DataIngestion(
                data_ingestion_config =  self.data_ingestion_config
            )

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from URL")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )

            return data_ingestion_artifact

        except Exception as e:
            raise SignException(e, sys)
        
    def run_pipeline(self) -> None:
        try:
            logging.info("Starting the pipeline")
            data_ingestion_artifact = self.start_data_ingestion()
            logging.info("Pipeline completed")
            

        except:
            logging.error(f"Pipeline failed due to: {Exception}")
            raise Exception("Your data is not in correct format")
        