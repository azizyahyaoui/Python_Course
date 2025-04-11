print("------------------------------------ Datetime----------------------------------------------------")

import datetime as dt


date = dt.date(2025, 1, 2)
today = dt.date.today()

time = dt.time(12, 30, 0)
now = dt.datetime.now()

now = now.strftime("%H:%M:%S %m-%d-%Y" )

#target_datetime = dt.datetime(2031,3,22)
target_datetime = dt.datetime(2020,3,22)
current_time = dt.datetime.now()


if target_datetime < current_time:
  print("Target date has passed")
else:
  print("Target date has not passed")









print()
print("--------------------------------------------------------------------------------------------------------")