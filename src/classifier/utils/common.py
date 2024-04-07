import os
from box.exceptions import BoxValueError
import yaml
from src.classifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    reads a yaml file and returns a ConfigBox
    Args:
    path_to_yaml (str): path to yaml file

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
    ConfigBox: ConfigBox object type
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Loaded config from {path_to_yaml} successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True) -> None:
    """
    Args:
        path_to_directories (list) : list of directories to create
        ignore_log(bool, optional) : ignore if multiple directories to be created. Defaults to True
    :return:
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at {path}")


@ensure_annotations
def save_json(path: Path, content: dict) -> None:
    """
    Saves JSON data
    Args:
        path (Path) : path to json file
        data (dict) : data to be saved in the json file
    """
    with open(path, 'w') as f:
        json.dump(content, f, indent=4)

    logger.info(f"Saved json at {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads JSON data
    Args:
        path (Path) : path to json file
    Returns:
        ConfigBox : data as class attributes insted of a dictonary
    """
    with open(path, 'r') as f:
        content = json.load(f)
    logger.info(f"Loaded json file from : {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """
    Saves binary file
    Args:
        data (Any) : data to be saved as binary file
        path (Path) : path to the binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Saved binary at : {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads binary data
    Args:
        path (Path) : path to the binary file
    Returns:
        Any: Objects stored in the file
    """
    data = joblib.load(filename=path)
    logger.info(f"Loaded binary from : {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Gets the size in KBs
    Args:
        path (Path) : path to the file
    Returns:
        str: size in KBs
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, 'rb') as f:
        return base64.b64encode(f.read())
