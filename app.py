from ObjectDetectionJetson.logger import logging
from ObjectDetectionJetson.exception import AppException
import sys

try:
    a = 3 / "s"

except Exception as e:
    raise AppException(e, sys)


# logging.info("Custom log test")