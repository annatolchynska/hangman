#  💀 HANGMAN_GAME 💀
---
HANGMAN is a guessing Python terminal game, which runs in the mock terminal on Heroku.

Users try to find out the secret word by suggesting letters or the whole word within a certain number of guesses.

### HOW TO PLAY
The word to guess is shown by a row of dashes representing each letter of the word. 
If the player suggests a letter which occurs in the word, the letter appears in the correct position. If the suggested letter does not occur in the word, the computer adds one element of a hanged stick figure as a tally mark. The player may, at any time, attempt to guess the whole word. Generally, the game ends once the word is guessed, or if the stick figure is complete — signifying that all guesses have been used.

## FEATURES
---
### Existing features
* welcoming message and request to enter the player's name by input
* explaining the rules of the game and display of the hidden word with an empty gallows
* accepts user's input 
* input validation 
   * user cannot enter a word that has more or less letters than the hidden word
   * the program informs the user if the letter is already used
   * the game gives user the feedback when the letter/word is correct/incorrect
* the end game message which informs of winning/loosing
* request input to start new game or exit

### Future features


