############################################################
# CMPSC 442: Uninformed Search
############################################################

student_name = "Tisya Vaidya"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import math
import random
import copy
import queue 



############################################################
# Section 1: N-Queens
############################################################

def num_placements_all(n):
    if n == 0:
        return 1
    else:
        return n * num_placements_all(n - 1)

def num_placements_one_per_row(n):
    return n**n

def n_queens_valid(board):
    n= len(board)
    if n == 1:
        return True
    for i in range(n):
        a = board[i]
        if a in board[i + 1:]:
            return False
        for j in range(i + 1, n):
            if abs(i - j) == abs(a - board[j]):
                return False
    return True

def n_queens_helper(board, depth, n):
    if depth == n:
        return [board[:]]  
    else:
        solutions = []
        for i in range(n):
            board.append(i)
            if n_queens_valid(board):
                solutions.extend(n_queens_helper(board, depth + 1, n))  
            board.pop()  
        return solutions

def n_queens_solutions(n):
    for solution in n_queens_helper([], 0, n):
        yield solution

        
############################################################
# Section 2: Lights Out
############################################################

class LightsOutPuzzle(object):

    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])

    def get_board(self):
        return self.board

    def perform_move(self, row, col):
        max_row = len(self.board)
        max_col = 0
        if max_row > 0:
            max_col = len(self.board[0])
        self.board[row][col] = not self.board[row][col]
        if row - 1 >= 0:
            self.board[row - 1][col] = not self.board[row - 1][col]
        if col - 1 >= 0:
            self.board[row][col - 1] = not self.board[row][col - 1]
        if col + 1 < max_col:
            self.board[row][col + 1] = not self.board[row][col + 1]
        if row + 1 < max_row:
            self.board[row + 1][col] = not self.board[row + 1][col]

    def scramble(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if random.random() < 0.5:
                    self.perform_move(row, col)
                    
    def is_solved(self):
        for row in self.board:
            for switch in row:
                if switch:
                    return False
        return True

    def copy(self):
        return copy.deepcopy(self)

    def successors(self):
        for row in range(self.rows):
            for col in range(self.cols):
                new_puzzle = self.copy()
                new_puzzle.perform_move(row, col)
                yield (row, col), new_puzzle

    def __eq__(self, other):
        return isinstance(other, LightsOutPuzzle) and self.board == other.board

    def __hash__(self):
        return hash(tuple(map(tuple, self.board)))

    def find_solution(self):
        explored = set()
        q = queue.Queue()
        q.put((self, []))

        while not q.empty():
            puzzle, path = q.get()

            if puzzle.is_solved():
                return path

            if puzzle not in explored:
                explored.add(puzzle)

                for move, successor in puzzle.successors():
                    q.put((successor, path + [move]))
        return None 

def create_puzzle(rows, cols):
    board = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(False)
        board.append(row)
    return LightsOutPuzzle(board)


############################################################
# Section 3: Linear Disk Movement
############################################################



def solve_identical_disks(length, n):

    
    initial_state = tuple(range(n))
    q = queue.Queue()
    q.put((initial_state, []))
    visited_states = set([initial_state])
    while not q.empty():
        current_state, current_moves = q.get()
        if tuple(sorted(current_state)) == tuple(range(length - n, length)):
            return current_moves
        for i in range(n):

            # Move type 
            # Next block is empty and if you are going over length L


            # Move type 2
            # Next block occupied, next nexxt block free and check lenght L

    
            # Move type 1: Move to an empty next block if within length L
            if current_state[i] + 1 < length and (current_state[i] + 1) not in current_state:
                new_state = list(current_state)
                new_state[i] += 1
                new_state = tuple(new_state)
                
                if new_state not in visited_states:
                    q.put((new_state, current_moves + [(current_state[i], new_state[i])]))
                    visited_states.add(new_state)
                    
            # Move type 2: Move over an occupied block if next block is free and within length L
            if current_state[i] + 2 < length and  (current_state[i] + 1) in current_state and (current_state[i] + 2) not in current_state:
                new_state = list(current_state)
                new_state[i] += 2
                new_state = tuple(new_state)
                
                if new_state not in visited_states:
                    q.put((new_state, current_moves + [(current_state[i], new_state[i])]))
                    visited_states.add(new_state)

    return "No solution found."






def solve_distinct_disks(length,n):
    initial_state= tuple(range(n))
    q=queue.Queue()
    q.put((initial_state, []))
    visited_states = set([initial_state])
    while not q.empty():
        current_state, current_moves = q.get()
        print(current_state, current_moves)
        if current_state[::-1] == tuple(range(length - n, length)):
            return current_moves
        
        for i in range(n):
            if current_state[i] + 1 < length and (current_state[i] + 1) not in current_state:
                new_state = list(current_state)
                new_state[i] += 1
                new_state = tuple(new_state)
                
                if new_state not in visited_states:
                    q.put((new_state, current_moves + [(current_state[i], new_state[i])]))
                    visited_states.add(new_state)
                    
            # Move type 2: Move over an occupied block if next block is free and within length L
            if current_state[i] + 2 < length and  (current_state[i] + 1) in current_state and (current_state[i] + 2) not in current_state:
                new_state = list(current_state)
                new_state[i] += 2
                new_state = tuple(new_state)
                
                if new_state not in visited_states:
                    q.put((new_state, current_moves + [(current_state[i], new_state[i])]))
                    visited_states.add(new_state)
            #Move 3
            if current_state[i] - 1 >= 0 and (current_state[i] - 1) not in current_state:
                new_state = list(current_state)
                new_state[i] -= 1
                new_state = tuple(new_state)
                
                if new_state not in visited_states:
                    q.put((new_state, current_moves + [(current_state[i], new_state[i])]))
                    visited_states.add(new_state)
                    
            # Move type 4: 
            if current_state[i] - 2 >= 0 and  (current_state[i] -1) in current_state and (current_state[i] -2) not in current_state:
                new_state = list(current_state)
                new_state[i] -= 2
                new_state = tuple(new_state)
                
                if new_state not in visited_states:
                    q.put((new_state, current_moves + [(current_state[i], new_state[i])]))
                    visited_states.add(new_state)

    return "No solution found."
                
          
