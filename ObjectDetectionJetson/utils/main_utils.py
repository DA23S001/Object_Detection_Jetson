import os.path
import sys
import yaml
import base64

from ObjectDetectionJetson.exception import AppException
from ObjectDetectionJetson.logger import logging

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yamL_file:
            logging.info("Read yaml file successfully")
            return yaml.safe_load(yamL_file)
        
    except Exception as e:
        raise AppException(e, sys) from e
    


def write_yaml_file(file_path: str, content: object, replace: bool=False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            yaml.dump(content, file)
            logging.info("Successfully write_yaml_file")\
            
    except Exception as e:
        raise AppException(e, sys)
    

def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open("./data/" + filename, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
    
    