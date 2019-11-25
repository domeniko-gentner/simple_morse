# simple_morse

Simple Morse Program to show the use of a dict in Python.

### How it works

All morse codes are in a dict in morse_dict.py. This is used to translate any text to morse.
White Spaces are signed by a simple pause. Normally, you are supposed to do a minute pause between characters and a longer pause between words.

This is honored in this script by a 5 second pause between words.

The sound is generated via a Windows function. So this won't work right away on Unix.
Anyway, it is for education, not practical use.


### Exercises:

* Make the script stop for 1 second after each whole character has been sounded

