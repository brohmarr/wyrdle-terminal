# Wyrdle (Terminal)
# by: @brohmarr
# 
# Python v3.12.3

import pathlib
import random
from string import ascii_letters


# Reading the list of words available.
WORDS = pathlib.Path("wordlist.txt")

# Turning the retrieved words into a list for the secret word to be selected from.
word_list = [
    word.upper()
    for word in WORDS.read_text(encoding="utf-8").split("\n")
    if len(word) == 5 and all(letter in ascii_letters for letter in word)
]

# Selecting a secret word from the word list.
word = random.choice(word_list)

# For testing purposes...
print("TESTING: THE SECRET WORD IS", word)

ATTEMPTS = 6

for attempt in range(1, ATTEMPTS + 1):
    # Getting the input word from the player.
    guess = input(f"\nGuess {attempt}: ").upper()

    # Making sure the player only types in words with 5 letters.
    while len(guess) != 5:
        guess = input(f"The word contains 5 letters, try again. Guess {attempt}: ").upper()

    # Checking if the player guessed the word correctly.
    if guess == word:
        print("Correct")
        
        break

    # Checking the individual letters of the guess for the clues.
    correct_letters = {letter for letter, other_letter in zip(guess, word) if letter == other_letter}
    misplaced_letters = (set(guess) & set(word) - correct_letters)
    wrong_letters = set(guess) - set(word)

    # Showing the player the clues for their current guess.
    print("Correct letters:", ", ".join(correct_letters))
    print("Misplaced letters:", ", ".join(misplaced_letters))
    print("Wrong letters:", ", ".join(wrong_letters))

else:
    # Telling the player what the secret word when they exhaust their attempts.
    print(f"\nThe correct word was {word}.")
