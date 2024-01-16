## Overview
This Python application provides a graphical interface for the classic 8 Queens puzzle, where the goal is to place eight queens on a chessboard in such a way that no two queens threaten each other. Utilizing the tkinter library for the GUI, it offers interactive features to place queens randomly and solve the puzzle using a stochastic hill climbing algorithm.

## Features
- Graphical representation of an 8x8 chessboard.
- Interactive placement of queens on the chessboard.
- Ability to shuffle queens randomly.
- Implementation of the stochastic hill climbing algorithm to solve the puzzle.
- Display of the number of conflicts (queens threatening each other) on the board.

![8-queens_hill_climbing](https://github.com/RafaBrito008/8-Queens_Hill_Climbing/assets/94416107/c6b415c5-9989-4668-a1ba-114f20bd2df8)

## Requirements
- Python 3.x
- tkinter library (usually included in standard Python installations)

## Usage
1. Run the script to start the application.
2. Click the "Mezclar" button to randomly place the queens on the chessboard.
3. Click the "Siguiente" button to perform a hill climbing step and move towards solving the puzzle.
4. The application will indicate when the puzzle is solved (no conflicts) or if a local optimum is reached.
