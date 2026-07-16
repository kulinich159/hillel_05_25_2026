from  constantas import BASE_PROJECT_PATCH
import logging
import logging.config
import os
config_file_path = os.path.join(BASE_PROJECT_PATCH, "logging_config.ini")

logging.config.fileConfig(config_file_path) # берем конфіг звідси

logger = logging.getLogger("sampleLogger")

logger.debug('This is DEBUG log level')
logger.info('This is INFO log level')
logger.error('This is ERROR log level')