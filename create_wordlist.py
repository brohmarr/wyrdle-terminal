# Wyrdle (Terminal)
# by: @brohmarr
# 
# Python v3.12.3

import pathlib
import sys
from string import ascii_letters


# The two variables below serve the purpose of holding the text files
# being received from the user when running this script, as shown below:
# 
# $ python3 create_wordlist.py [path_in] [path_out]
# 
# path_in represents the text file to be read, with all the possible
#         words.
# path_out represents the text file where this script will write the
#          filtered words from the file at path_in.
path_in = pathlib.Path(sys.argv[1])
path_out = pathlib.Path(sys.argv[2])

# This list is used to hold a filtered version of all the words in the
# input file (path_in). It uses a default len of 5 characters as the
# output file is intended to be used for a "Wordle"-like game.
words = sorted(
    {
        word.lower()
        for word in path_in.read_text(encoding="utf-8").split()
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    },
    key=lambda word: (len(word), word),
)
path_out.write_text("\n".join(words))
