# Hangman Game

import random , time

words = ("python", "java", "easy", "duck", "apple", "carrot","banana", "phone", "computer", "cat")
hangman_art = {
    0: ("     ",
        "     ",
        "     "),
    1: ("  o  ",
        "     ",
        "     "),
    2: ("  o  ",
        "  |  ",
        "     "),
    3: ("  o  ",
        " /|  ",
        "     "),
    4: ("  o  ",
        " /|\\ ",
        "     "),
    5: ("  o  ",
        " /|\\ ",
        " /   "),
    6: ("  o  ",
        " /|\\ ",
        " / \\ ")
}

def display_hangman(wrong_guesses):
    print("=============The hang court: =============")
    for row in hangman_art[wrong_guesses]:
        print(row)
    print("==========================================")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))













def main():
    print()
    print("-------------------------------------------------------------------------------------------------")
    print("Welcome to Hangman Game!")
    print("You have to guess the word before  you run out of attempts.")
    print("Good Luck!")
    print("______________________________________________________________\n")

    answer = random.choice(words).lower()
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_hangman(wrong_guesses)
        display_hint(hint)
        

        print()
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("===========================================================")
            print("|     Invalid input. Please enter a single letter.        |")
            print("===========================================================")
            time.sleep(2)
            continue
        if guess in guessed_letters:
            print("===========================================================")
            print("|     You've already guessed that letter. Try another.    |")
            print("===========================================================")
            time.sleep(2)
            continue
        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1


        if "_" not in hint:
            display_hint(hint)
            print()
            print("================================================================")
            print(f"|     Congratulations! You've guessed the word: {answer}!     |")
            print("================================================================")
            time.sleep(2)
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print("===============================================")
            print("|     Game Over!, Better luck next time!      |")
            print("===============================================")
            is_running = False
        










    print()
    print("-------------------------------------------------------------------------------------------------")
if __name__ == "__main__":
    main()