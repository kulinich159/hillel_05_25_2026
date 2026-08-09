import time
import pytz
from datetime import datetime, UTC

print(time.time())
print(time.localtime())

cur_date = time.localtime()

print(cur_date.tm_year)
print(cur_date.tm_mon)
print(cur_date.tm_mday)
print(cur_date.tm_zone)
print(cur_date.tm_sec)

print(f"Now is {cur_date.tm_hour}:{cur_date.tm_min}:{cur_date.tm_sec}")

cur_time = time.time()

# while time.time() - cur_time < 10:
#     print("sending request...")
#     time.sleep(0.5)

print("--datetime-"*10)


row1 = "2026-08-03 19:49:30" #UTC ISO format
row2 = "24-08-03 19:49:30.200" #UTC



print(datetime.now())
print(type(datetime.now()))

row1_dt = datetime.fromisoformat(row1)
# row2_dt = datetime.fromisoformat(row2) - не ысо формат
row11_dt = datetime.strptime(row1, "%Y-%m-%d %H:%M:%S")
row22_dt = datetime.strptime(row2, "%y-%m-%d %H:%M:%S.%f")
print(row1_dt.date())
print(row1_dt.time())
print(row11_dt)
print(row2)
print(row22_dt)

data = datetime.now(UTC)

print(data.tzname())

cur_time_with_tz = time.localtime()
print(cur_time_with_tz.tm_zone)

client_time = "24-08-03 19:49:30.200"
server_time = "24-08-03 19:49:30.200+00:00"


# print(pytz.all_timezones)


client_time_dt = datetime.strptime(client_time, "%y-%m-%d %H:%M:%S.%f")
server_time_dt = datetime.strptime(server_time, "%y-%m-%d %H:%M:%S.%f%z")
client_time_dt_with_tz = pytz.timezone("Europe/Kyiv").localize(client_time_dt)

print(client_time_dt)
print(client_time_dt_with_tz)
# print(server_time_dt - client_time_dt)
