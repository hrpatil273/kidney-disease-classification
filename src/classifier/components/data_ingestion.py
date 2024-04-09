import os
import zipfile
import gdown
from classifier import logger
from classifier.entity.config_entity import DataIngestionConfig
from classifier.utils.common import get_size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self) -> str:
        """
        Fetch data from the Source URL
        :return:
        """
        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_files
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} to {zip_download_dir}")

            file_name = dataset_url.split("/")[-2]
            prefix_url = "https://drive.google.com/uc?/export=download&id={}".format(file_name)
            gdown.download(prefix_url, zip_download_dir)
            logger.info(f"Extracting data from {dataset_url} to {zip_download_dir}")
        except Exception as e:
            logger.error(f"{e}")
            raise e

    def extract_zip_files(self):
        """
        Extract the zip files in the artifacts directory
        :param: zip_file_path: path of the zip file
        :return: None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_files, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"File unzipped at {unzip_path}")