"""
Import random word from the list in words.py
"""
# The code was taken from youtube tutorial "how to build a hangman
# in 10 min with Python" by Kite
# https://github.com/kiteco/python-youtube-code/blob/master/build-hangman-in-python/hangman.py
import random
import os
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
    print("-------------------------------------------------------")
    print("{:^70}".format("Welcome to \u2620  HANGMAN_GAME! \u2620 \n"))
    print("-------------------------------------------------------")
    print("YOU HAVE TO GUESS WORD BY ONE LETTER AT A TIME,\n")
    print("YOU ONLY HAVE SIX TRIES OTHERWISE YOU'LL BE HANGED \n")
    print("-------------------------------------------------------")
    print("{:^70}".format("HAVE FUN !"))
    while True:
        name = input("Please enter your name: ").upper()
        if name.isalpha():
            clear_board()
            game(get_word())
        else:
            print("PLEASE USE LETTERS ONLY")


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
        guess = input("Please guess a letter or word: \n").upper()
        if len(guess) == 1 and guess.isalpha():
            # When the letter aleady has been used
            if guess in guessed_letters:
                print("YOU'VE ALREADY GUESSED THE LETTER", guess)
            # In case of incorrect answer
            elif guess not in word:
                print("UNFORTUNATELY YOU'RE ONE STEP CLOSER TO BEING HANGED..")
                lives -= 1
                guessed_letters.append(guess)
            # In case of correct letter
            else:
                print("WELL DONE!", guess, "IS IN THE WORD!")
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
                print("YOU'VE CORRECTLY GUESSED THE WORD", guess)
            # In case of incorrect guessing the word
            elif guess != word:
                print(guess, "IS WRONG!")
                lives -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_complete = word
        # In case of invalid input (number, space)
        else:
            print("NOT A VALID GUESS.")
        print(hangman_pics(lives))
        print(word_complete)
        print("\n")
    if guessed:
        print("CONGRATS! YOU GUESSED THE WORD! YOU WIN! \U0001F3C6")
        while True:
            play_again = input('Play Again? ( Y / N ) : ').upper()
            if play_again == 'Y':
                game(get_word())
            elif play_again == 'N':
                welcome_board()
            else:
                print('Please choose option Y or N ')
    else:
        print("SORRY \U0001F62D YOU LOST! \n")
        print("THE WORD WAS " + word + ". SEE YOU IN THE AFTERLIFE \U0001F480")
        while True:
            play_again = input('Play Again? ( Y / N ) : ').upper()
            if play_again == 'Y':
                game(get_word())
            elif play_again == 'N':
                welcome_board()
            else:
                print('Please choose option Y or N ')


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
    while input("Play Again? (Y/N) ").upper() == "Y":
        clear_board()
        welcome_board()
        word = get_word()
        game(word)


if __name__ == "__main__":
    main()
