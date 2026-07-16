import logging

file_handler = logging.FileHandler("error.log")
file_handler.setLevel(logging.ERROR)
file_formatter = logging.Formatter("Custom formater: %(name)s - %(asctime)s - %(levelname)s -  %(message)s")
file_handler.setFormatter(file_formatter)

# Створення конфігурації
logging.basicConfig(level=logging.DEBUG,
                    format='!!!!!!! %(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.StreamHandler(),  # Виведення в консоль
                        logging.FileHandler('example.log'),  # Запис у файл
                        file_handler
                    ])

# Використання логера
logger = logging.getLogger(__name__)

logger.debug('This message level DEBUG')
logger.info('This message level INFO')
logger.error('This message level ERROR')