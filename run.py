# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Import random word from the list in words.py
import random 
from words import word_list

def get_word():
    """
    Defines random word from the words in words.py file
    """
    word = random.choice(word_list)
    return word

def play(word):
    """
    The function running the game
    """
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Welcome to Hangman game!\n")
    print("You have to guess random word by one letter at a time\n")
    print("You only have six tries otherwise you'll be hanged /n")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")