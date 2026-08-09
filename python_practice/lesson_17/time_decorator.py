import random
import time
from turtledemo.penrose import start


def time_checker(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print(f"It takes {end_time - start_time} to execute function")
        return result
    return wrapper

@time_checker
def send_request_to_db():
    print("sending request")
    time.sleep(random.choice(range(2)))

for _ in range(5):
    send_request_to_db()