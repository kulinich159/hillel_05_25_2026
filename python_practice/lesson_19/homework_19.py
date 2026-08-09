import logging
from datetime import datetime

logging.basicConfig(filename="hb_test.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_row_with_correct_key(file_name):
    filtered_log = []
    with open(file_name) as file:
        log_content = file.read().splitlines()
        for row in log_content:
            if "Key TSTFEED0300|7E3E|0400" in row:
                filtered_log.append(row)
        return filtered_log

def logging_row_with_correct_time_period(some_list):
    start_timestamp = None

    for row in some_list:
        word_timestamp_index = row.find("Timestamp ")
        time_in_row = row[word_timestamp_index + len("Timestamp "): word_timestamp_index + len("Timestamp ") + 8]
        current_timestamp = datetime.strptime(time_in_row, "%H:%M:%S")

        if start_timestamp is not None:
            delta_time = (start_timestamp - current_timestamp).total_seconds()

            if 31 < delta_time < 33:
                logging.warning(f"{row}")
            elif delta_time >= 33:
                logging.error(f"{row}")

        start_timestamp = current_timestamp

    print(f"Результат записано в файл hb_test.log")

logging_row_with_correct_time_period(find_row_with_correct_key("hblog.txt"))