import random
import copy

class Board: 
    def __init__(self): 
        self.board = [[0] * 9 for _ in range(9)]
    
    def check(self, lst): # checks rows 
        for i in range(1, 10): 
            if lst.count(i) > 1: 
                return False
        return True

    def sq(self, coordinates, number):
        box_x = coordinates[1] // 3
        box_y = coordinates[0] // 3

        for y in range(box_y * 3, box_y * 3 + 3):
            for x in range(box_x * 3, box_x * 3 + 3):
                if number == self.board[y][x] and (y, x) != coordinates:
                    return False

        return True

    def valid(self, row, col, num): 
        # Check row
        if num in self.board[row]:
            return False
        # Check column
        if num in [self.board[i][col] for i in range(9)]:
            return False
        # Check 3x3 square
        if not self.sq((row, col), num):
            return False
        return True

    def generate_board(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    random_nums = list(range(1, 10))
                    random.shuffle(random_nums)
                    for num in random_nums:
                        if self.valid(row, col, num):
                            self.board[row][col] = num
                            if self.generate_board():
                                return True
                            self.board[row][col] = 0
                    return False
        return True

    def remove_tiles(self, difficulty=30):
        tile_removed = 0 
        attempts = 0 
        while tile_removed < difficulty and attempts < 100:
            row, col = random.randint(0,8), random.randint(0,8)
            if self.board[row][col] != 0:
                backup = self.board[row][col]
                self.board[row][col] = 0

                if self.count_solutions() == 1:
                    tile_removed +=1
                else: 
                    self.board[row][col] = backup
                attempts += 1

                

    def solve(self, count=False):
        empty = self.find_empty()

        if not empty:
            return 1 if count else True
        
        row, col = empty
        solutions = 0
        for num in range(1, 10):
            if self.valid(row, col, num):
                self.board[row][col] = num
                if count: 
                    solutions += self.solve(count=True)
                    if solutions > 1: 
                        break
                else: 
                    if self.solve():
                        return True
                self.board[row][col] = 0
        return solutions if count else False


    def find_empty(self):
        for row in range(9): 
            for col in range(9):
                if self.board[row][col] == 0:
                    return (row, col)
        return None

    def print_board(self):
        for row in self.board:
            print(row)

    def count_solutions(self):
        # Make a deep copy of the board to avoid modifying the original
        board_copy = copy.deepcopy(self.board)
        solvable = self.solve(count=True)
        # Restore the original board
        self.board = board_copy
        return solvable

# Generate a Sudoku board
# sudoku_board = Board()
# sudoku_board.generate_board()
# sudoku_board.print_board()