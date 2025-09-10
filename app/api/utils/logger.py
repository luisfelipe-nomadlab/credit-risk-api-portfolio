import logging
import sys
from pythonjsonlogger import jsonlogger

def get_logger(name: str = "fraud_detection"):

    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        logHandler = logging.StreamHandler(sys.stdout)
        formatter = jsonlogger.JsonFormatter(
            "%(asctime)s %(levelname)s %(name)s %(message)s"
        )
        logHandler.setFormatter(formatter)
        logger.addHandler(logHandler)
        logger.setLevel(logging.INFO)

    return logger

logger = get_logger()
logger.info("Logger configurado com sucesso!")