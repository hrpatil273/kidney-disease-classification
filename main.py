from classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.classifier import logger


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e