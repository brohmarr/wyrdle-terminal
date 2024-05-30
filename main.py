# Wyrdle (Terminal)
# by: @brohmarr
# 
# Python v3.12.3

import pathlib
import random
from string import ascii_letters


# This variable holds the path to the wordlist.
WORDS = pathlib.Path("wordlist.txt")

# This list serves the purpose of letting us choose a random word from
# the wordlist.
word_list = [
    word.upper()
    for word in WORDS.read_text(encoding="utf-8").split("\n")
    if len(word) == 5 and all(letter in ascii_letters for letter in word)
]

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
    guesses = []

    # Process.
    for attempt in range(1, ATTEMPTS + 1):
        guess = input(f"\nGuess {attempt}: ").upper()

        while True:
            if len(guess) != 5:
                input_message = "Your guess must contain five letters, please, try again: "
                guess = input(input_message).upper()

                continue
            if guess in guesses:
                input_message = "You already guessed that word, please, try again: "
                guess = input(input_message).upper()

                continue

            break
        
        guesses.append(guess)
        guessed_correctly = check_guess(guess, word)

        if guessed_correctly:        
            break
    
    # Post-process.
    else:
        game_over(word)

def get_a_random_word():
    word = random.choice(word_list)

    # TODO: Adding this for testing purposes, remove it later...
    print("TESTING: THE SECRET WORD IS", word)

    return word

def check_guess(guess, word):
    if guess == word:
        print("Correct!")
        
        return True

    correct_letters = {letter for letter, other_letter in zip(guess, word)
                       if letter == other_letter}
    misplaced_letters = (set(guess) & set(word) - correct_letters)
    wrong_letters = set(guess) - set(word)

    print("Correct letters:", ", ".join(correct_letters))
    print("Misplaced letters:", ", ".join(misplaced_letters))
    print("Wrong letters:", ", ".join(wrong_letters))

    return False

def game_over(word):
    print(f"\nThe correct word was {word}.")

if __name__ == "__main__":
    main()
