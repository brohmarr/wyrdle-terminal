# Wyrdle (Terminal)

🔵 **Status:** Done

A clone of the famous game "Wordle", that runs in the terminal.

I developed this project to study [Rich](https://github.com/Textualize/rich), a Python library for "rich text and beautiful formatting in the terminal".

I intend to use this project as a base to start learning about [Kivy](https://github.com/kivy/kivy) in the near future, and port this project to mobile devices.

**NOTE:** This idea is currently on hold as I'm focusing on web development.

## Requirements

* Python (v3.12.5)
* Packages listed in [requirements.txt](requirements.txt), that can be installed with the following command:
    * ```pip install -r requirements.txt```

## Usage

* Clone this repository with the command below and cd into it in the terminal; or download it as a ".zip" file, using the green "<> Code" button above, unzip it and enter the unzipped folder;
    * ```git clone https://github.com/brohmarr/wyrdle-terminal```
* Run the [main.py](main.py) file with the command below and start playing! You can check the available words in [wordlist.txt](wordlist.txt) or change them automatically from another text file using the [create_wordlist.py](create_wordlist.py) script (you can read its documentation in the file itself).
    * ```python main.py```