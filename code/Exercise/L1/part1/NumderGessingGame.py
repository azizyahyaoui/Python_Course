import random

print("---------------------------------------------------------------------------------------")

lowest_number = 1
highest_number = 100

answer = random.randint(lowest_number, highest_number)
guesses = 0
is_running = True

print("______________________________________")
print("    Number Guessing Game:    ")
print("______________________________________")

print(f"Please Select a number between {lowest_number} and {highest_number}")

while is_running:
  guess = input("Enter your guess: ")

  if guess.isdigit():
    guess = int(guess)
    guesses += 1

    if guess < lowest_number or guess > highest_number:
      print("That number is out of the range!")
      print(f"Please Select a number between {lowest_number} and {highest_number}")
    elif guess < answer:
      print("Too low! try again! ")
    elif guess > answer:
      print("Too high! try again! ")
    else:
      print("CORRECT GUESS!")
      print(f"Number of guesses: {guesses}")
      is_running= False
  else:
    print("INVALID GUESS!")
    print(f"Please Select a number between {lowest_number} and {highest_number}")


print("---------------------------------------------------------------------------------------")