# Tic Tac Toe
Hello, World! Make sure you run OPTION 1 prior to running the rest of the code. Option 1 shows instructions on how to play the game.
# Purpose
* To make a playable game using a text based UI in Python, that the user can enjoy for hours of fun!

## Overview of Provided Code
Here is overview of files for "Tic Tace Toe" sample:
* Main.py: Menu for the project, First screen the user sees.
* game3x3.py: A game file, for the 3x3 game. The user can select which game they would like to play. This file contains the code for a classic 3x3 game.
* game4x4.py: Another game file.  This contains the links for a 4x4 Tic Tac toe game.
* instructions.py: Standard instructions file. Prints instructions for each game, respectively.
* gametests folder: Contains obsolete older version game4x4 and our code testing file.

## Map of Provided Code to AP CSA Requirements

| Strategy | Type | Implementation in game |
| ------------- | ----------- | ----------- |
|  Algorithms and Programming | Strings and Numbers | Numbers were incorporated in our project in many ways. We used numbers in print statements in the instructions. Perhaps our most prominent use of numbers in our project was for the game board. The game board runs by inputting the row number and column number to place the user’s marker. So if the user enters 1 and then 1, the marker will be placed in row 1 and column 1. In the 3x3 game, the numbers had to be reduced by 1 because there is one less row and column. |
|  Algorithms and Programming | Variables and Assignments | Some variables and assignments that we worked on were assigning colors to each player (X or O) and incorporating colors into the instructions to make it more distinguishable and organized. We also defined many variables like def drawboard which draws the board merging ascii characters with values in pos list. |
|  Algorithms and Programming | Lists, Dictionaries, and Arrays | We’ve made the game playable by using “if” statements and by including all possible column and row options, which means that if a spot is already marked, it cannot be marked again. When working on the 3x3 game, we used the same array/game board as the 4x4 game board (This is an example of a 2D array) |
|  Algorithms and Programming | Iteration | Essentially, our entire tic tac toe game is based on iterations. We mapped out each combination to win in both the 4x4 and 3x3 games, whether it be horizontal, vertical, or diagonal. Each time a player inputs their location for their marker (X or O), the code undergoes many iterations to exchange turns between the two players. Then, the code is able to recognize a winning combination and display a message saying “Player _ has won!”, which ends the iteration(s).  |
|  Algorithms and Programming | Functions |  One main Function we used was the clear screen function. It is located in the termy.py file. |
|  Algorithms and Programming | *** EXTRA CREDIT ***Classes and Object | In Python, objects are an encapsulation of variables and functions into a single entity, and the objects get their variables and functions from classes. Classes are essentially a template to create your objects. In this game, an example of classes and objects being used are in the game3x3.py file. In this file, in lines 43-51, we identified each row and column as a specific number from 0-2. This gave us three columns to choose from and three rows to choose from, labeled 0, 1, and 2. Then, we mapped out each winning combination in lines 53-55 of the same file, using these variables of 0, 1, and 2. By grouping these variables and using them to provide the code for each winning combination and to prompt the system to display the "winner's message", we were able to create a class with respective objects. |

## Authors
* Arul, Colin, Manuel, Pedro, Roop

## Version History
* 1.0
    * Initial Release
* week 3
    * Began working on extra gamemode 3x3/improving menu
* week 2
    * finishing the 4x4 tic tac toe
* week 1
    * began work on tic tac toe board
