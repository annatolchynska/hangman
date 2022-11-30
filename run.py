"""
Import random word from the list in words.py
"""
# The code was taken from youtube tutorial "how to build a hangman
# in 10 min with Python" by Kite
# https://github.com/kiteco/python-youtube-code/blob/master/build-hangman-in-python/hangman.py
import random
from words import word_list


def get_word():
    """
    Defines random word from the words in words.py file
    """
    word = random.choice(word_list).upper()
    return word


def game(word):
    """
    The welcoming function of the game
    """
    word_complete = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    lives = 6
    print("-------------------------------------------------------")
    print("Welcome to HANGMAN game!\n")
    print("-------------------------------------------------------")
    name = input("Please enter your name").upper()
    print("You have to guess random word by one letter at a time,\n" + name)
    print("You only have six tries otherwise you'll be hanged \n")
    print("-------------------------------------------------------")
    print("HAVE FUN," + name)
    print(display_hangman(lives))
    print(word_complete)
    print("\n")
    # Runs guessing process
    while not guessed and lives > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed the letter", guess)
                # When the letter aleady has been used
            elif guess not in word:
                print("Unfortunately you're one step closer to being hanged..")
                lives -= 1
                guessed_letters.append(guess)
            else:
                print("Well done!", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_complete)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_complete = "".join(word_as_list)
                if "_" not in word_complete:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You've correctly guessed the word", guess)
            elif guess != word:
                print(guess, "is wrong!")
                lives -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_complete = word
        else:
            print("Not a valid guess.")
        print(display_hangman(lives))
        print(word_complete)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you lost! \n")
        print("The word was " + word + ". See you in the afterlife:-)")


def display_hangman(lives):
    """
    displays the figure of hangman from the first try up to the sixth
    """
    levels = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
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
    word = get_word()
    game(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        game(word)


if __name__ == "__main__":
    main()

