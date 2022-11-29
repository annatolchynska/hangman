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
    The welcoming function of the game
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
   
    # Runs guessing process
   
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ")
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've guessed correctly", guess)
            elif guess not in word:
                print(guess, "Unfortunately you're one step closer to being hanged..")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Well done!", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You've correctly guessed the word", guess)
            elif guess != word:
                print(guess, "is wrong!")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you lost! The word was " + word + ". See you in the afterlife:-)")

def display_hangman(tries):
    """
    displays the figure of hangman
    """
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
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
    return stages[tries]

def main():
    """
    function that runs the game
    """
    word = get_word()
    play(word)
    while input("Play Again? (y/n) ") == "y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
