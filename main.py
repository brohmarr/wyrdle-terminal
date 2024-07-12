# Wyrdle (Terminal)
# by: @brohmarr
# 
# Python v3.12.3

import pathlib
import random
from string import ascii_letters
from rich.console import Console
from rich.theme import Theme

# Creating a variable to control rich's print function.
console = Console(width=48, height=16, theme=Theme({"error": "red", "tip": "blue"}))

# This variable holds the path to the wordlist.
WORDS = pathlib.Path("wordlist.txt")

# Choosing the secret word length for the game.
WORD_LENGTH = 5

# Choosing the number of attempts available to the user.
ATTEMPTS = 6

# This function contains the main loop of the game. It asks the user for
# their input, makes sure it's exactly 5 letters long and checks if they
# guessed the secret word correctly. If not, it shows them which letters
# they guessed correctly and in the right spot, which letters they
# guessed correctly in the wrong spot and which letters are not part of
# the secret word.
# 
# If the user exausts all of their attempts, it shows them the secret
# word.
def main():

    # Pre-process.
    word = get_a_random_word()
    guesses = ["_" * WORD_LENGTH] * ATTEMPTS
    words_guessed = []

    # Process.
    for idx in range(ATTEMPTS):
        tip_message = ""
        while True:
            display_game_page(idx=idx, word=word, guesses=guesses)

            if tip_message != "":
                console.print(tip_message, style="tip")
            guess = console.input("\nGuess word: ").upper()
            
            is_guess_valid, tip_message = check_for_valid_guess(guess=guess, words_guessed=words_guessed)
            if is_guess_valid:
                guesses[idx] = guess
                words_guessed.append(guess)
                break
                
        if guesses[idx] == word:
            break
    
    # Post-process.
    game_over(idx=idx, word=word, guesses=guesses, guessed_correctly=guesses[idx] == word)

def get_a_random_word():

    if word_list := [
        word.upper()
        for word in WORDS.read_text(encoding="utf-8").split("\n")
        if len(word) == WORD_LENGTH and all(letter in ascii_letters for letter in word)
    ]:
        return random.choice(word_list)
    else:
        console.print(f"No words of length {WORD_LENGTH} in the word list.", style="error")

        raise SystemExit()

def display_game_page(idx, word, guesses):

    refresh_page(headline=f"Guess {idx+1}", word=word)
    show_guesses(guesses, word)

def refresh_page(headline, word):

    console.clear()
    
    # TODO: Adding this for testing purposes, remove it later...
    console.print(f"TESTING: The secret word is {word}!\n")
    
    console.rule(f":mage: {headline} :mage:\n")

def show_guesses(guesses, word):

    console.print()
    for guess in guesses:
        styled_guesses = []
        for letter, correct in zip(guess, word):
            if letter == "_":
                style = "bold white"
            elif letter == correct:
                style = "bold white on green"
            elif letter in word:
                style = "bold white on yellow"
            else:
                style = "bold white on #676767"
            styled_guesses.append(f"[{style}]{letter}[/]")
        
        console.print("".join(styled_guesses), justify="center")

def check_for_valid_guess(guess, words_guessed):

    if len(guess) != WORD_LENGTH:
        return False, f"\nTip: the word is {WORD_LENGTH} letters long."
    elif guess in words_guessed:
        return False, "\nTip: you already guessed that word."
    else:
        for letter in guess:
            if not letter in ascii_letters:
                return False, "\nTip: only letters are accepted as characters."
    
    return True, None

def game_over(idx, word, guesses, guessed_correctly):
    
    display_game_page(idx=idx, word=word, guesses=guesses)

    if guessed_correctly:
        console.print(f"\nCongrats! You guessed the word! :tada:")
    else:
        console.print(f"\nSorry, the secret word was {word}.")

if __name__ == "__main__":
    main()
