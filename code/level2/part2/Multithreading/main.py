print("------------------------------------ Multithreading ----------------------------------------------------")

import threading, time

def feeding_cat(name,meal, num_process):
  print(f"Process '{num_process}' in progress ...")
  time.sleep(5)
  print(f"You finish putting meal '{meal}' for your cat '{name}'")

def cleaning_yard(num_process):
  print(f"Process '{num_process}' in progress ...")
  time.sleep(9)
  print("The back yard is clean.")


def checking_mailbox(num_process):
  print(f"Process '{num_process}' in progress ...")
  time.sleep(9)
  print("You get all the mails.")



th1 = threading.Thread(target=feeding_cat, args=("Michou","chunk raw meat",1))
th1.start()
th2 = threading.Thread(target=checking_mailbox, args=(2,))
th2.start()
th3 = threading.Thread(target=cleaning_yard, args=(3,))
th3.start()

th1.join()
th2.join()
th3.join()

print()


print()
print("--------------------------------------------------------------------------------------------------------")
