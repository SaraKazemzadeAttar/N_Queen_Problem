# N-Queens Problem Solver

## Description

This Python script solves the N-Queens problem using a brute-force approach and visualizes the solutions using Pygame. The N-Queens problem is a classic puzzle that involves placing N chess queens on an N×N chessboard so that no two queens threaten each other. In chess, a queen can attack horizontally, vertically, and diagonally.

## About N-Queens Problem

In the N-Queens problem, the challenge is to place N chess queens on an N×N chessboard in such a way that no two queens threaten each other. This means that no two queens can share the same row, column, or diagonal. The problem is a classic example of a constraint satisfaction problem and has applications in various fields including mathematics, computer science, and artificial intelligence.

However, it's important to note that the brute-force method used in this script may not be efficient for large values of N due to its exponential time complexity.

## Code Explanation

The provided Python script consists of functions to solve the N-Queens problem and to visualize the solutions using Pygame. Here's a brief overview of the code:

- `generate_permutations(sequence)`: Generates all permutations of the given sequence, where each number represents the column position of a queen and the index represents the row position.
- `is_valid_permutation(perm)`: Checks if a permutation is valid, ensuring that no two queens threaten each other.
- `solve_n_queens(n)`: Solves the N-Queens problem by generating all permutations of queen positions and filtering out the valid solutions.
- `get_input()`: Uses Pygame to get user input for the number of queens.
- Pygame setup for input handling and visualization of the chessboard and queens.
- The main loop that handles Pygame events and displays the solutions.

## Instructions

### Run the Script

Execute the script using a Python interpreter.

### Input

Upon running the script, a Pygame window will prompt you to enter the number of queens. Please type the desired number of queens and press "Enter".

### Navigation

After entering the number of queens, press the "Space" key to cycle through the solutions.

### Exit

You can exit the program by closing the Pygame window or by pressing the "Esc" key.

**Note:** The program doesn't provide solutions for 2 or 3 queens due to their inherent nature. Ensure to press "Enter" before pressing "Space" to start the visualization.
