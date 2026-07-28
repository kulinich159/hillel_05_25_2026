import json
import pathlib
import os
import logging

logging.basicConfig(filename="json_Kulinich.log", level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

dir_with_json_files = os.path.join(str(pathlib.Path().absolute().parent), "ideas_for_test", "work_with_json")

for file in os.listdir(dir_with_json_files):
    file_path = os.path.join(dir_with_json_files, file)
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            json.load(file)
    except json.JSONDecodeError as e:
        logging.error(f"JSON file {file_path} is incorrect: {e}")

