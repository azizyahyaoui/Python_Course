import time

timer = int(input("Enter time in seconds: "))

for T in range(timer, 0, -1):
  seconds = T % 60
  minutes = int(T /60) % 60
  hours = int(T / 3600)
  print(f"{hours:02}:{minutes:02}:{seconds:02}")
  time.sleep(1)

print("TIME's UP !")