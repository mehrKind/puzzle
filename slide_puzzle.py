import numpy as np
import heapq

class Puzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = np.array(initial_state)
        self.goal_state = np.array(goal_state)

    def get_possible_moves(self):
        moves = []
        empty_pos = np.argwhere(self.initial_state == 0)[0]
        emp_row, emp_col = empty_pos
        
        if emp_row > 0:
            moves.append("up")
        if emp_row < 2:
            moves.append("down")
        if emp_col > 0:
            moves.append("left")
        if emp_col < 2:
            moves.append("right")

        return moves
        

    def make_move(self, direction):
        empty_pos = np.argwhere(self.initial_state == 0)[0]
        emp_row, emp_col = empty_pos

        if (direction == "up") and (emp_row > 0):
            self.initial_state[emp_row][emp_col],  self.initial_state[emp_row-1][emp_col]= self.initial_state[emp_row -1][emp_col], self.initial_state[emp_row][emp_col]
        elif (direction == "down") and (emp_row < 2):
            self.initial_state[emp_row][emp_col], self.initial_state[emp_row + 1][emp_col] = self.initial_state[emp_row + 1][emp_col], self.initial_state[emp_row][emp_col]
        elif (direction == "right") and (emp_col < 2):
            self.initial_state[emp_row][emp_col], self.initial_state[emp_row][emp_col+1] = self.initial_state[emp_row][emp_col + 1], self.initial_state[emp_row][emp_col]
        elif (direction == "left") and (emp_col > 0):
            self.initial_state[emp_row][emp_col],  self.initial_state[emp_row][emp_col -1]= self.initial_state[emp_row][emp_col -1], self.initial_state[emp_row][emp_col]

    def is_goal(self):
        return np.array_equal(self.initial_state, self.goal_state)

    def heuristic(self):
        h = 0
        for i in range(3):
            for j in range(3):
                if self.initial_state[i, j] != 0:
                    goal_row, goal_col = divmod(self.initial_state[i, j] - 1, 3)
                    h += abs(i - goal_row) + abs(j - goal_col)
        return h

def search_alg(puzzle):
    queue = []
    visited = set()
    heapq.heappush(queue, (puzzle.heuristic(), puzzle.initial_state.tolist()))

    while queue:
        _, current_state = heapq.heappop(queue)
        current_state = np.array(current_state)
        print(current_state)

        if np.array_equal(current_state, puzzle.goal_state):
            return True

        visited.add(str(current_state.tolist()))
        temp_puzzle = Puzzle(current_state.tolist(), puzzle.goal_state.tolist())

        for move in temp_puzzle.get_possible_moves():
            temp_puzzle.make_move(move)

            if str(temp_puzzle.initial_state.tolist()) not in visited:
                heapq.heappush(queue, (temp_puzzle.heuristic(), temp_puzzle.initial_state.tolist()))

            temp_puzzle.make_move({"up": "down", "down": "up", "left": "right", "right": "left"}[move])

    return False

state = [[1, 4, 6], [8, 7, 0], [2, 3, 5]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

puzzle = Puzzle(state, goal)

if search_alg(puzzle):
    print("The puzzle is solvable!")
else:
    print("The puzzle is not solvable.")

