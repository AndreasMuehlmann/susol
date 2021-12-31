Susol

License: MIT
Creator: Andreas Mühlmann
Also on Github for latest changes: https://github.com/AndreasMuehlmann/susol

Susol is a programm to solve a sudoku riddle or to give you hints while solving one. If you don't know what sudoku is or how it works,
look here: https://de.wikipedia.org/wiki/Sudoku

Quickstart:
    - Make a riddle to be solved:
	- Create a new file:
        - Type the riddle that you want to have solved into the file.
        - one line is one row.
        - seperate the columms by spaces
        - Every square can contain an "e" for an empty square or
           a number from 1 to 9 for a number.
        - The file has to be in the same directory as the programm

    Example:
    2 3 9 e e e 4 1 e
    4 6 e e 2 e 9 e e
    e e 5 e 1 e e 3 e
    6 e e 1 8 e e e e
    e e 8 e 4 e 3 e 5
    e e e e 9 2 e e 1 
    e 5 e e 3 e 1 e e
    e e 4 e 5 e e 8 3
    e 9 6 e e e 5 4 2

    -open a terminal and make sure your in the directory of the programm
    -run the programm by typing ".\susol.exe <filename>" into the terminal
    -to get hints run the programm with ".\susol.exe <filename> -h"