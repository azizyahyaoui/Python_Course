import random

print("---------------------------------------------------------------------------------------")

print("__________________________")
print("   DICE GAME:    ")
print("__________________________")

print()

# Dice face representations using ASCII art
dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘",
    ),
}


dice = []
total = 0
number_of_dice = int(input("How many dice?: "))

for die in range(number_of_dice):
  dice.append(random.randint(1, 6))

for line in range(5):
  for die in dice:
    print(dice_art.get(die)[line], end="")
  print()

for die in dice:
  total += die
print(f"total: {total}")















print()
print("---------------------------------------------------------------------------------------")

