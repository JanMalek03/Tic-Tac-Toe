# Tic-Tac-Toe (3x3)

This is a simple Python implementation of the classic Tic-Tac-Toe game with a 3x3 grid.
It allows two players to take turns making moves and checks for a win or draw.
Additionally, there is an AI opponent that plays as 'O'.

## Table of Contents

- [Getting Started](#getting-started)
- [How to Play](#how-to-play)
- [AI Opponent](#ai-opponent)
- [Learnings and Takeaways](#learnings-and-takeaways)
- [Contributing](#contributing)


## Getting Started

To run the game, you need to have Python installed on your computer. You can download and install Python from [the official website](https://www.python.org/downloads/).
To start the game, simply run the following command in command line:

    python Tic_Tac_Toe_3x3.py


## How to Play

The game is played on a 3x3 grid. Players take turns making their moves, with 'X' representing the first player and 'O' the second. The first player to get 3 of her marks in a row (up, down, across, diagonally) is the winner.
Players input the row and column of their move, where valid input ranges from 1 to 3 (e.g., 2 than 1 to place your mark in the second row, first column).
The game continues until a player wins or it ends in a draw.
If you want to play again, just run the code again.


## AI Opponent

The AI opponent (marked as 'O') uses the minimax with [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) algorithm to make strategic moves.
It calculates the best move by exploring different possibilities and choosing the most optimal one.
On a 3x3 grid, the AI plays perfectly, so unfortunately for you, you can't beat it (of course, you can try).


## Learnings and Takeaways

Through the development of this Tic-Tac-Toe game, I have improved my skills in several areas:

- **Minimax Algorithm**: Understanding the minimax decision rule for predicting moves and its implementation for the AI opponent.
- **Alpha-Beta Pruning**: Learning about optimizing the minimax algorithm by pruning unnecessary branches in the search tree, thus improving AI efficiency.
- **Python Code Quality**: Focused on writing clear and organized code, making the code easier to read and maintain.

This project has been an excellent exercise in applying algorithmic thinking and Python programming to create a functional, enjoyable game. It stands as a practical example of my coding approach, with opportunities for further expansion and improvement.



## Contributing

Contributions to this project are welcome. If you want to improve the game or add new features, feel free to fork this repository and submit a pull request.

Enjoy playing the game!
