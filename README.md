# Minesweeper-probabilty-calculator
A Python implementation of Minesweeper with a mine probability calculator

## Requirements
This Python project uses PyGame, SymPy and in-built math functions for Python >= 3.8

## How to use
- The game currently does not have a proper GUI. It starts with the game already initiated according to the number of mines, width and height determined in the code. To change these variables go to the lines 4, 5 and 6 of main.py. To change the window size, change the variable 'SQ_SIZE' in line 14.
- Click with the left mouse button to reveal a square. If it is a mine, all the mines will appear and the game will freeze.
- Click with the right mouse button to add or remove a flag (**Warning**: squares incorrectly flagged may crash the game when using the probability function due to the linear system having inconsistencies, see more about below)
- Press 'p' to show the probabilities of the border squares
- Press 'l' to hide the probabilities
- Press 'c' to automatically click the squares with probability of 100% or 0%

## How the probability calculator works
The function that calculates probability is separed in 3 steps:
