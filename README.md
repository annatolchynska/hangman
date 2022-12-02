# <h1 align ="center">__💀 HANGMAN_GAME 💀__</h1>
---
[live link is here]()

HANGMAN is a guessing Python terminal game, which runs in the mock terminal of Code Institute on Heroku.

Users try to find out the secret word by suggesting letters or the whole word within a certain number of guesses.

## HOW TO PLAY

The word to guess is shown by a row of dashes representing each letter of the word. 
If the player suggests a letter which occurs in the word, the letter appears in the correct position. If the suggested letter does not occur in the word, the computer adds one element of a hanged stick figure as a tally mark. The player may, at any time, attempt to guess the whole word. Generally, the game ends once the word is guessed, or if the stick figure is complete — signifying that all guesses have been used.

---
### User Experience(UX)

First Time User Goals. 
* As a First Time Visitor, I want to easily navigate through the game.
* As a First Time Visitor, I want to enjoy the process, have fun, feel vintage vibes when playing.
* As a First Time Visitor, I want to be able to make sure I don't get repeated words.
 
Returning user goals
* As a Returning User, I want to be able to guess the words I haven't guessed before.
* As a Returning User, I want the navigation to be the same as it was the first time to keep it familiar.

Site owner Goals.
* As a Site owner, I want the game to have simple rules
* As a Site owner, I want the site to be easily navigated
* As a Site owner, I want the words not to be repeated

### Flowchart
---

<img src = "./readme_images/hangman.jpeg" alt = "img of the flowchart">
    
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
* keep scores of different players
* add an option for player to choose a topic for words to make this game more educational for users who are learning English
* make it possible to play multiplayers game
---

### Technology Used
* [Python programming language](https://en.wikipedia.org/wiki/Python_(programming_language))
* [Github](https://github.com/)
* [Gitpod](https://gitpod.io/)
* [Lucidchart](https://www.lucidchart.com/)
* [Heroku](https://www.heroku.com) 

---
### Testing
* PEP8CI Python Validator:
no significant errors were returned when passing through PEP8CI - [Website here](https://pep8ci.herokuapp.com/#)
 
 <img src ="./readme_images/pep8validation.png" alt ="img of pep8 validation">

* Tested the code in the Code Institute Heroku terminal and also the terminal inside of Gitpod.
* Checked that symbols, numbers or empty spaces are coming up as invalid guesses when guessing the word.

---
### Bugs and unfixed bugs
While running the game I had the problem with a messy terminal. Fortunately, I found the solution with a function that clears terminal. No other bugs were found.

---
### Deployment
* Fork or clone this repository.
* Go to the Heroku Dashboard.
* Click New.
* Select create a new app.
* Set the buildbacks to Python and NodeJS in that order.
* Link the Heroku app to the repository.
* Click on Deploy.

---
### Credits
* unicode for emojis was taken from [FileFormat.info](https://www.fileformat.info/)
* the code for the game mostly was taken from Youtube tutorial ["how to build a hangman
in 10 min with Python" by Kite](https://www.youtube.com/watch?v=m4nEnsavl6w) and [GitHub kiteco](https://github.com/kiteco/python-youtube-code/blob/master/build-hangman-in-python/hangman.py)
* the code for function which clears the terminal was taken from these [sheets](http://www.coding4you.at/inf_tag/beginners_python_cheat_sheet.pdf)




