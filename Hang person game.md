# Hang person game

## RECOMMENDED PRIOR UNDERSTANDING

## RECOMMENDED PACKAGES

## RECOMMENDED RESOURCES

Get a file with words to use for your game from:

https://pbaumgarten.com/uploads/python/hangman-words.txt


Get the Python code for your Hangman pictures from:

https://pbaumgarten.com/python-sample-hangman-text

## TASK ONE

| Example special word | Example letters guessed | Example output |
| -------------------- | ------------------------| --------------------- |
| `"secret"` | `["a","b","c","d","e"]` | `"_e__e_"` |
| `"elephant"` | `["a","e","s","n","t"]` | `"e_e__ant"` |

## TASK TWO

## TASK THREE

## ATTRIBUTION/CREDIT


To build this exercise, you will need to successfully complete the following:
* Load the words text file into a Python list
* Use the random number generator to randomly select one item from the list as the secret word
* Reveal the secret word hiding the letters not yet guessed (see below for sample code on this)
* Use a while loop to keep asking the player to guess a new letter
* If a guessed letter is not in the secret word, increase their wrong guesses count and draw the new
hangman.
* If a guessed letter is in the word, add it to your list of correct guesses.
To help you get started, the following function will return a string that can be used to show the length of the secret word and the correct guesses.
