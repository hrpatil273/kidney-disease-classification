from classifier import logger
from classifier.components.data_ingestion import DataIngestion
from classifier.config.configuration import ConfigurationManager

STAGE_NAME = "Data Ingestion Stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
            config = ConfigurationManager()
            logger.info(f"Configuration loading completed")
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_files()
            logger.info("Stage 1 data ingestion completed")


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e