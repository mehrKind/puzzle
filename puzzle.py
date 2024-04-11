#?  ----------------------------------------
#    alireza mehraban (Slide Puzzle)
#            2024 - 04 - 11
# -----------------------------------------

import pygame
import sys
import numpy as np
import heapq

class Puzzle:
    def __init__(self, initial_state, goal_state):
        # Initialize the puzzle with the initial state and the goal state
        self.initial_state = np.array(initial_state)
        self.goal_state = np.array(goal_state)

    def get_possible_moves(self):
        # Get all the possible moves from the current state
        moves = []
        empty_pos = np.argwhere(self.initial_state == 0)[0]  # Find the position of the empty tile (0)
        emp_row, emp_col = empty_pos  # Get the row and column of the empty tile
        
        # Check the possible moves based on the position of the empty tile
        if emp_row > 0:
            moves.append("up")
        if emp_row < 2:
            moves.append("down")
        if emp_col > 0:
            moves.append("left")
        if emp_col < 2:
            moves.append("right")

        return moves  # Return the possible moves

    def make_move(self, direction):
        # Make a move in the given direction
        empty_pos = np.argwhere(self.initial_state == 0)[0]  # Find the position of the empty tile (0)
        emp_row, emp_col = empty_pos  # Get the row and column of the empty tile

        # Swap the empty tile with the adjacent tile based on the direction
        if (direction == "up") and (emp_row > 0):
            self.initial_state[emp_row][emp_col],  self.initial_state[emp_row-1][emp_col]= self.initial_state[emp_row -1][emp_col], self.initial_state[emp_row][emp_col]
        elif (direction == "down") and (emp_row < 2):
            self.initial_state[emp_row][emp_col], self.initial_state[emp_row + 1][emp_col] = self.initial_state[emp_row + 1][emp_col], self.initial_state[emp_row][emp_col]
        elif (direction == "right") and (emp_col < 2):
            self.initial_state[emp_row][emp_col], self.initial_state[emp_row][emp_col+1] = self.initial_state[emp_row][emp_col + 1], self.initial_state[emp_row][emp_col]
        elif (direction == "left") and (emp_col > 0):
            self.initial_state[emp_row][emp_col],  self.initial_state[emp_row][emp_col -1]= self.initial_state[emp_row][emp_col -1], self.initial_state[emp_row][emp_col]

    def is_goal(self):
        # Check if the current state is the goal state
        return np.array_equal(self.initial_state, self.goal_state)

    def heuristic(self):
        # Calculate the heuristic value (Manhattan distance) for the current state
        h = 0
        for i in range(3):
            for j in range(3):
                if self.initial_state[i, j] != 0:
                    goal_row, goal_col = divmod(self.initial_state[i, j] - 1, 3)  # Get the goal position for the current tile
                    h += abs(i - goal_row) + abs(j - goal_col)  # Calculate the Manhattan distance
        return h  # Return the heuristic value

    def animate_moves(self, moves):
        # Animate the moves
        for move in moves:
            self.make_move(move)  # Make the move
            screen.fill(BACKGROUND_COLOR)  # Fill the screen with the background color
            draw_grid()  # Draw the grid
            pygame.display.flip()  # Update the full display surface to the screen
            pygame.time.wait(500)  # Wait for 500 milliseconds
    
    def is_solvable(self):
        # Check if the puzzle is solvable
        # Flatten the initial state and remove the zero
        flat_state = self.initial_state.flatten()
        flat_state = flat_state[flat_state != 0]

        # Count the inversions
        inversions = sum(1 for i in range(len(flat_state)) for j in range(i+1, len(flat_state)) if flat_state[i] > flat_state[j])

        # The puzzle is solvable if the inversion count is even
        return inversions % 2 == 0
def search_alg(puzzle):
    # This function implements the A* search algorithm to find the shortest path to the goal state
    queue = []  # Priority queue to store the states to be explored
    visited = set()  # Set to store the visited states
    heapq.heappush(queue, (puzzle.heuristic(), puzzle.initial_state.tolist(), []))  # Push the initial state to the queue

    while queue:
        # Pop the state with the lowest heuristic value
        _, current_state, path = heapq.heappop(queue)
        current_state = np.array(current_state)

        # Check if the current state is the goal state
        if np.array_equal(current_state, puzzle.goal_state):
            return path  # Return the path to the goal state

        # Add the current state to the visited set
        visited.add(str(current_state.tolist()))
        temp_puzzle = Puzzle(current_state.tolist(), puzzle.goal_state.tolist())

        # Explore all possible moves from the current state
        for move in temp_puzzle.get_possible_moves():
            temp_puzzle.make_move(move)

            # If the new state has not been visited, add it to the queue
            if str(temp_puzzle.initial_state.tolist()) not in visited:
                heapq.heappush(queue, (temp_puzzle.heuristic(), temp_puzzle.initial_state.tolist(), path + [move]))

            # Undo the move to explore other moves
            temp_puzzle.make_move({"up": "down", "down": "up", "left": "right", "right": "left"}[move])

    return []  # Return an empty list if no path to the goal state is found

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 300, 300  # Dimensions of the window
BACKGROUND_COLOR = (0, 0, 0)  # Color of the background
SQUARE_COLOR = (255, 255, 255)  # Color of the squares
TEXT_COLOR = (0, 0, 0)  # Color of the text
SQUARE_SIZE = WIDTH // 3  # Size of the squares

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("slide puzzle")

# Set up the font
font = pygame.font.Font(None, 36)

def draw_grid():
    # This function draws the grid on the screen
    for i in range(3):
        for j in range(3):
            # Draw the square and the number on it
            if puzzle.initial_state[i, j] == 0:
                pygame.draw.rect(screen, (240,240,240), pygame.Rect(j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))  # Change the background color of the square containing the zero
                text = font.render(" ", True, TEXT_COLOR)  # Display nothing for the zero
            else:
                pygame.draw.rect(screen, SQUARE_COLOR, pygame.Rect(j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                text = font.render(str(puzzle.initial_state[i, j]), True, TEXT_COLOR)
            screen.blit(text, (j * SQUARE_SIZE + SQUARE_SIZE // 2 - text.get_width() // 2, i * SQUARE_SIZE + SQUARE_SIZE // 2 - text.get_height() // 2))

state = [[1, 2, 6], [4, 7, 0], [8, 3, 5]]  # Initial state of the puzzle
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Goal state of the puzzle

puzzle = Puzzle(state, goal)  # Create a Puzzle object
if puzzle.is_solvable():
    # If the puzzle is solvable, find the solution and animate the moves
    moves = search_alg(puzzle)
    puzzle.animate_moves(moves)
else:
    # If the puzzle is not solvable, print a message and exit the program
    print("not solveable")
    sys.exit()

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If the user closes the window, quit the game
            pygame.quit()
            sys.exit()

    # Draw the grid and update the screen
    screen.fill(BACKGROUND_COLOR)
    draw_grid()
    pygame.display.flip()
