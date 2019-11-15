"""

Logic flow of this game

* Get all the words from the file
* Pick a random number between 0 and the number of words
* Use the random number to select our secret word
* Generate the hint text
* While points lost < 6 and the secret has not been fully guessed
    * Show the player the hint
    * Show the player their guesses so far
    * Ask the player to guess a letter
    * Update the set of guesses so far with the new guess
    * If the guess is correct
        * Print a congratulatory message
    * Otherwise
        * Print a message of doom and gloom
        * Update points lost
        * Print the hangman picture based on current points lost
    * Generate the updated hint text
* Game is over!














"""




























import random
import files
import hangman_pics

n = 0
print( hangman_pics.HANGMAN_PICS[ n ] )

all_words = files.read("words_list.txt")






    guess = input("Guess a letter:      ")
    guesses = guesses + guess



























def get_secret_word_hint( secret, guesses ):
    hint = ""
    for letter in secret:
        if letter in guesses:
            hint = hint + letter
        else:
            hint = hint + "_"
    return hint

all_words = files.read("words_list.txt")
r = random.randint(0, len(all_words)-1)
secret = all_words[r].lower()
game_over = False
guesses = ""
points_lost = 0
hint = get_secret_word_hint( secret, guesses )
while points_lost < 6 and hint != secret:
    print("Secret word hint:    ",hint)
    print("Your guesses so far: ",guesses)
    guess = input("Guess a letter:      ").lower()
    guesses = guesses + guess
    if guess in secret:
        print("Well done, the letter",guess,"is in the secret word!")
    else:
        print("Sorry, you've just lost a limb!")
        points_lost += 1
        print( hangman_pics.HANGMAN_PICS[ points_lost ] )
    hint = get_secret_word_hint( secret, guesses )
print("Game over!")
print("The secret word was: ",secret)



