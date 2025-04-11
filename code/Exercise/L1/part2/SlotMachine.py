# Slot Machine Game

import random, time

def spin_wheel():
    symbols = ['🍒','🍋', '🍉', '🍓','🍌', '🔔','⭐',]
    return [random.choice(symbols) for _ in range(4)]

def print_wheel(wheel):
    print("******************")
    print(" | ".join(wheel))
    print("******************")

def get_reward(wheel, bet) ->int:
    if wheel[0] == wheel[1] == wheel[2] == wheel[3]:
        if wheel[0] == '🍒':
            return bet * 3
        elif wheel[0] == '🍋':
            return bet * 4
        elif wheel[0] == '🍉':
            return bet * 5
        elif wheel[0] == '🍓':
            return bet * 6
        elif wheel[0] == '🍌':
            return bet * 7
        elif wheel[0] == '🔔':
            return bet * 10
        elif wheel[0] == '⭐':
            return bet * 20
    else:
            return 0



def main():

    balance = 100
    is_playing = True

    print()
    print("-------------------------------------------------------------------------------------------------")
    print("________________________________________")
    print("🎰 Welcome to the Slot Machine Game 🎰")
    print(" Symbols:    🍒 🍋 🍉 🍓 🍌 🔔 ⭐   ")
    print("________________________________________")

    while balance > 0:
        print("*********************************")
        print(f"Your current Balance: ${balance}")
        print("*********************************")
        time.sleep(1)
        print()

        bet = input("Place your bet amount: $")

        if not bet.isdigit():
            print("==============================================")
            print("|        Invalid input. Try again.           |")  
            print("==============================================")
            time.sleep(2)
            continue

        bet = int(bet)
        if bet <= 0:
            print("===========================================================")
            print("|    Bet amount must be greater than 0 ! . Try again.     |")
            print("===========================================================")
            time.sleep(2)
            continue
        
        if bet > balance:
            print("==========================================================")
            print("|    Bet amount exceeds your balance. Try again.         |")
            print("==========================================================")
            time.sleep(2)
            continue

        balance -= bet
        print("Spinning the wheel...\n")
        time.sleep(2)

        wheel = spin_wheel()
        print_wheel(wheel)

        reward = get_reward(wheel, bet)
        if reward > 0:
            print("==============================================")
            print(f"Congratulations! You won ${reward}")
            print("----------------------------------------------")
            balance += reward
            print(f"Your current Balance: ${balance}")
            print("==============================================")
            time.sleep(2)
        else:
            print("==============================================")
            print("|    You won nothing! Better luck next time! |")
            print("==============================================")
            time.sleep(2)

        print("_________________________________________________________")
        keep_playing = input("Do you want to play again? (Y/N): ").upper()
        print("_________________________________________________________")
        if keep_playing not in ["YES", "Y"]:
            break

    print("==============================================")
    print("Game Over!, Thanks for playing the game!")
    print(f"Your final balance: ${balance}")
    print("==============================================")

    print()
    print("-------------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    main()