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
The function that calculates probability is separed in 3 main steps:
- First, it uses the basic rules to determine if a square has a mine, such as the a fact that if the number of unknown surrounding squares is the same number of the cell, then all of them are mines, or the fact that if the number of known mines around a square is the same number the square, then all the other surrounding ones are safe
- Then, a more complex rule using the idea of sets is used (see https://youtu.be/8j7bkNXNx4M) to determine the location of even more mines and safe squares
- If even after these two rules not every square has been determined to have a mine or not, then a linear system of equations is created for the entire game. The idea is that every border square can be labelled (see image below).

![image](https://user-images.githubusercontent.com/52111108/208491177-d28e1145-50af-4f88-b41c-e4364ace1dc5.png)

Using the image above, the following equations, for example, can be used:
- a1+a2 = 1
- a1+a2+a3 = 2
- a2+a3+a4 = 2
- and so on

Therefore, the game can be treated as a system of equations. In this project, SymPy was used to handle the system, giving as output a parametric solution with a certain number of parameters. For example (**not** the solution for the image above), a solution can be given as (a1-1, a1, a2, a1+a2, a4, a4-1), that is, a0 = a1-1, a3 = a1+a2 and a5 = a4-1, in this case. 

This solution is then broken down in groups that are independent between each other, that is, the parameters of each group do not appear in any of the other expressions of the parametric solution. In the previous example, the groups would be [[a1,a2], [a4]] and the groups expressions would be [[a1-1, a1, a2, a1+a2], [a4, a4-1]].

Then, for each group, all possible values of their respective parameters (note that each parameter is either 0 or 1) are tested, and those which satisfy the property that the result of each expression is also either 0 or 1 is saved. So, in the previous example, each time a1=0 the result would not be considered, because then a1-1 would be -1. 

After this, every possible combination of the found group solutions, that is, every possible arrangement of the mines in the border squares, is considered to calculate the final probability of each square. The calculation is identical to the one described here: https://youtu.be/D7Cwbk9xphY

For the squares that are not adjacent to a number square, the probability calculation is much more simple because there isn't much information. Their probabilities, given the number of mines used in a certain arrangement of the border squares, is simply (the remaining mines - number of mines used in the arrangement)/(non-border squares), as the mines must be scattered equally likely for each one of them. Then, the final probability is the average over all possible arrangements.
