import random

print("---------------------------------------------------------------------------------------")

print("___________________________________________")
print("   ROCK, PAPER, SCISSORS GAME:    ")
print("___________________________________________")
print()

opts = ("rock", "paper", "scissors")
is_playing = True

while is_playing:

  player = None
  computer = random.choice(opts)

  while player not in opts:
    player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player choice: {player}")
    print(f"Computer choice: {computer}")

  if player == computer:
    print("It's a tie!")
  elif player == "rock" and computer == "scissors":
    print("You win!")
  elif player == "paper" and computer == "rock":
    print("You win!")
  elif player == "scissors" and computer == "paper":
    print("You win!")
  else:
    print("You lose!")


  if not (input("Play again? (y/n): ").lower()) == "y":
    is_playing = False

print("Thanks for playing!")











print("---------------------------------------------------------------------------------------")
