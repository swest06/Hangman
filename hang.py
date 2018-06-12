import random
from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')


def game():
    words = ["banana", "grape", "orange", "mango", "cherry", "apple", "pear", "peach"]
    strikes = int(7)
    play = True

    while play:
        secret = random.choice(words)
        g_guess = []
        b_guess = []

        while len(b_guess) < strikes and len(g_guess) != len(list(secret)):
            clear()
            print("A random fruit has been chosen.\n"
                  "Try to guess what it is. \n")

            # Prints correct letters and empty spaces
            for i in secret:
                if i in g_guess:
                    print(i, end=" ")
                else:
                    print("_", end=" ")

            # Get guess
            print("strikes: " + str(len(b_guess)) + "/7")
            guess = input("Guess a letter: ").lower()

            if len(guess) !=1:
                print("you can only enter 1 letter")
                continue
            elif guess in b_guess or guess in g_guess:
                print("You've already guessed that letter")
                continue
            elif not guess.isalpha():
                print("You can only guess letters")
                continue

            # Compare good guesses with word
            if guess in secret:
                [g_guess.append(guess) for i in secret if i == guess]

                if len(g_guess) == len(list(secret)):
                    print("you win {}".format(secret))
                    play = False
                    break
            else:
                b_guess.append(guess)
        else:
            print("You lose. The word was {}.".format(secret))
            play = False


def main():
    play = True
    while play:
        game()
        replay = input("Play again? y/n: ")
        if replay[0].lower() == "y":
            continue
        else:
            play = False
            print("Goodbye.")


if __name__ == "__main__":
    main()
