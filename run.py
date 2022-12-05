"""
Import random word from the list in words.py
"""
# The code was taken from youtube tutorial "how to build a hangman
# in 10 min with Python" by Kite
# https://github.com/kiteco/python-youtube-code/blob/master/build-hangman-in-python/hangman.py
import random
import os
from art import tprint
from words import word_list


def get_word():
    """
    Defines random word from the chosen topic words.py file
    """
    word = random.choice(word_list).upper()
    return word


def clear_board():
    """
    Function that clears the terminal. Sourced from:
    http://www.coding4you.at/inf_tag/beginners_python_cheat_sheet.pdf
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome_board():
    """
    The welcoming function of the game
    """
    clear_board()
    print("-----------------------------------------------------------------")
    tprint("_WELCOME__TO_ \n", font="cybermedium")
    tprint("_HANGMAN_GAME_! \n", font="cybermedium")
    print("-----------------------------------------------------------------")
    print("_YOU_HAVE_TO_GUESS_WORD_BY_ONE_LETTER_AT_A_TIME_,\n")
    print("_YOU_ONLY_HAVE_SIX_TRIES_OTHERWISE_YOU'LL_BE_HANGED_ \n")
    print("-----------------------------------------------------------------")
    print("\U0001F480_HAVE__FUN_ !\U0001F480 ")
    print("-----------------------------------------------------------------")
    while True:
        try:
            name = input("_Please_enter_your_name_: \n").upper()
            if name.isalpha():
                clear_board()
                game(get_word())
                break
            else:
                print("_PLEASE_USE_LETTERS_ONLY_")
        except ValueError:
            print("_SOMETHING_WENT_WRONG_")


def game(word):
    """
    The game itself
    """
    word_complete = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    lives = 6
    print(hangman_pics(lives))
    print(word_complete)
    print("\n")
    # Runs guessing process
    while not guessed and lives > 0:
        guess = input("_Please_guess_a_letter_or_word_: \n").upper()
        if len(guess) == 1 and guess.isalpha():
            # When the letter aleady has been used
            if guess in guessed_letters:
                print("_YOU'VE_ALREADY_GUESSED_THE_LETTER_", guess)
            # In case of incorrect answer
            elif guess not in word:
                print("_UNFORTUNATELY_YOU'RE_ONE_STEP_CLOSER_")
                print("_TO_BEING_HANGED_")
                lives -= 1
                guessed_letters.append(guess)
            # In case of correct letter
            else:
                print("_WELL_DONE!_", guess, "_IS_IN_THE_WORD!_")
                guessed_letters.append(guess)
                # Replace dashes with correctly guessed letters
                word_as_list = list(word_complete)
                ind = [i for i, letter in enumerate(word) if letter == guess]
                for index in ind:
                    word_as_list[index] = guess
                word_complete = "".join(word_as_list)
                if "_" not in word_complete:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            # In case of correct guessing the word
            if guess in guessed_words:
                print("_YOU'VE_CORRECTLY_GUESSED_THE_WORD_", guess)
            # In case of incorrect guessing the word
            elif guess != word:
                print(guess, "_IS_WRONG!_")
                lives -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_complete = word
        # In case of invalid input (number, space)
        else:
            print("_NOT_A_VALID_GUESS_")
            print("_PLEASE_USE_LETTERS_ONLY_")
        print(hangman_pics(lives))
        print(word_complete)
        print("\n")
    if guessed:
        print("---------------------------------------------------")
        print('\U0001F3C6 \U0001F3C6 \U0001F3C6 \U0001F3C6 \U0001F3C6')
        tprint("_CONGRATS!_", font="cybermedium")
        tprint("YOU WIN!_ ", font="cybermedium")
        print('\U0001F3C6 \U0001F3C6 \U0001F3C6 \U0001F3C6 \U0001F3C6')
        print("---------------------------------------------------")
        while True:
            try:
                play_again = input('_Play_Again?_ ( Y / N ) : \n').upper()
                if play_again == 'Y':
                    clear_board()
                    game(get_word())
                elif play_again == 'N':
                    welcome_board()
                else:
                    print('_Please_choose_option_Y_or_N_')
            except ValueError:
                print("_SOMETHING_WENT_WRONG_")
    else:
        print("---------------------------------------------------")
        print("\U0001F480 \U0001F480 \U0001F480 \U0001F480 \U0001F480")
        tprint("_SORRY_YOU_LOST!_", font="cybermedium")
        tprint("_SEE_YOU_...\n", font="cybermedium")
        tprint("...IN_THE_AFTERLIFE_ \n", font="cybermedium")
        print("_THE_WORD_WAS_" + word + "\n")
        print("\U0001F480 \U0001F480 \U0001F480 \U0001F480 \U0001F480")
        print("---------------------------------------------------")
        while True:
            try:
                play_again = input('_Play_Again?_ ( Y / N ) : \n').upper()
                if play_again == 'Y':
                    clear_board()
                    game(get_word())
                elif play_again == 'N':
                    welcome_board()
                else:
                    print('_Please_choose_option_Y_or_N_')
            except ValueError:
                print("SOMETING_WENT_WRONG_")


def hangman_pics(lives):
    """
    displays the figure of hangman from the first try up to the sixth
    """
    levels = [  # six wrong guesses: game over
                """
                   --------
                   |      |
                   |      O
                   |     /|\\
                   |      |
                   |     / \\
                   -
                """,
                # five wrong guesses
                """
                   --------
                   |      |
                   |      O
                   |     /|\\
                   |      |
                   |     /
                   -
                """,
                # four wrong guesses
                """
                   --------
                   |      |
                   |      O
                   |     /|\\
                   |      |
                   |
                   -
                """,
                # three wrong guesses
                """
                   --------
                   |      |
                   |      O
                   |     /|
                   |      |
                   |
                   -
                """,
                # two wrong guesses
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # one wrong guess
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # state when the game starts
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return levels[lives]


def main():
    """
    function that runs the game and gives the options
    to run it again or exit
    """
    welcome_board()
    word = get_word()
    game(word)
    while input("Play Again? (Y/N) \n").upper() == "Y":
        clear_board()
        welcome_board()


if __name__ == "__main__":
    main()
