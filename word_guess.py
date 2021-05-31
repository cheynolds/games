# Word Guessing

"""
File: word_guess.py
-------------------
When the user plays WordGuess, the computer first selects a secret
word at random from a list built into the program. The program then 
prints out a row of dashes—one for each letter in the secret word 
and asks the user to guess a letter. If the user guesses a letter 
that is in the word, the word is redisplayed with all instances 
of that letter shown in the correct positions, along with any 
letters correctly guessed on previous turns. If the letter does 
not appear in the word, the user is charged with an incorrect guess. 
The user keeps guessing letters until either (1) the user has 
correctly guessed all the letters in the word or (2) the user 
has made eight incorrect guesses. 
"""

import random

LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with

def play_game(secret_word):
    missed_let = ""
    correct_let = ""
    num_guess = INITIAL_GUESSES
    while num_guess > 0:
        show_current_word(missed_let, correct_let, secret_word)
        print("You have", num_guess, "guesses left")
        guess = user_guess(missed_let + correct_let)

        if guess in secret_word:
            print("That guess is correct.")
            correct_let = correct_let + guess
            
            found_all = True
            for i in range(len(secret_word)):
                if secret_word[i] not in correct_let:
                    found_all = False
                    break
            if found_all:
                print("Congratulations, the word is ", secret_word)
                num_guess = 0
        else:
            missed_let = missed_let + guess
            print("There are no", guess+"'s in the word")
            num_guess -= 1

def user_guess(all_guessed):
    #asks user for guess, rejects multi-char
    guess = input("Type a single letter here, then press enter: ")
    if len(guess) > 1:
        guess = input("Guess should only be a single character.")
    elif False:
        pass
        #check for already guessed 
    else:
        return guess.upper()

def show_current_word(missed_letters, correct_let, secret_word):
    blanks = '-' * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_let:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
    
    print("The word now looks like this: ", blanks)

def user_word(secret_word):
    pass
    return (dashes_return)

def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    index = random.randrange(3)
    if index == 0:
        return 'HAPPY'
    elif index == 1:
        return 'PYTHON'
    else:
        return 'COMPUTER'


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """

    secret_word = get_word()
    play_game(secret_word)

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
