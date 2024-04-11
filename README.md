# 8-Puzzle Solver :rocket:

This is a Python project that solves the 8-puzzle game using the A* search algorithm. The puzzle is represented as a 3x3 grid, where each tile can be moved to an adjacent empty space.

## Project Structure :file_folder:

The project consists of a single Python script that contains the implementation of the puzzle and the search algorithm.

- `puzzle.py`: This script contains the `Puzzle` class, which represents the state of the puzzle, and the `search_alg` function, which implements the A* search algorithm.

## Features :sparkles:

- **A* Search Algorithm**: The project uses the A* search algorithm to find the shortest path to the goal state.
- **Pygame Visualization**: The project uses Pygame to visualize the puzzle and animate the solution.
- **Heuristic Function**: The project uses the Manhattan distance as a heuristic function to guide the search algorithm.
- **Solvability Check**: The project checks if the puzzle is solvable before trying to solve it.

## How to Run :running:

1. Install the required Python packages:

```bash
pip install pygame numpy
```

2. Run the script:
```bash
python puzzle.py
```

## Future Work :hammer_and_wrench:
- Improve the visualization.
- Add support for larger puzzles.
- Implement other search algorithms.
## License :page_with_curl:
This project is licensed under the MIT License.

## Contact :mailbox:
For any queries, feel free to reach out to me at `mr.kind1382@gmail.com`.

## Acknowledgements :clap:
Thanks to everyone who contributed to this project!
