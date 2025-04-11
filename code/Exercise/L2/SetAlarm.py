print("---------------------------------------------------------------------------------------")

import time, datetime as dt, pygame

def set_alarm(alarm_time):

  print(f"Alarm set for {alarm_time}")
  sound_file ="code/Exercise/L2/siren-sound.wav"
  is_running = True

  while is_running:
    current_time = dt.datetime.now().strftime("%H:%M:%S")
    print(f"Current time is: {current_time}")

    if current_time == alarm_time:
      print("Wake UP U Lazy CAT! 😴😬")

      pygame.mixer.init()
      pygame.mixer.music.load(sound_file)
      pygame.mixer.music.play()
      while pygame.mixer.music.get_busy():
        time.sleep(1)

      is_running = False

    time.sleep(1)

  print()
  print("---------------------------------------------------------------------------------------")

if __name__ == "__main__":
  alarm_time = input("Set the alarm time (HH:MM:SS): ")
  set_alarm(alarm_time)