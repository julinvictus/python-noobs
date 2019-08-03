#I mostly just copied each function from your solution
#and tried to understand the code

import os
import random

def parse_board(filename):
    f = open(board_filename)
    board = []
    for line in f.readlines():
        line = line.strip()
        row = line.split(' ')
        board.append(row)
    return board
    #I still dont know what this function do

class SudokuGame:
    def __init__(self, board_filename):
        self.board = parse_board(board_filename)
        self.solution = parse_board(board_filename + "_solved")
        print(self.solution)
        #what does this function do?

    def __str__(self):
        # TODO: Return a string representation of this SudokuGame board!
        header = "      1 2 3   4 5 6   7 8 9\n\n"
        result = header
        i = 1
        for row in self.board:
            row_str = str(i) + "     "
            j = 1
            for col in row:
                row_str += col
                if j % 3 == 0:
                    row_str += "   "
                else:
                    row_str += " "
                j += 1
            result += row_str
            if i % 3 == 0:
                result += "\n\n"
            else:
                result += "\n"
            i += 1
        return result

    def check(self):
        header = "      1 2 3   4 5 6   7 8 9\n\n"
        result = header
        i = 1
        for row in self.board:
            row_str = str(i) + "     "
            j = 1
            for col in row:
                # If the base had this one solved, no coloring needed
                if self.base[i - 1][j - 1] != '_' or col == '_':
                    row_str += col
                elif self.board[i - 1][j - 1] == self.solution[i - 1][j - 1]:
                    row_str += green(col)
                else:
                    row_str += red(col)
                if j % 3 == 0:
                    row_str += "   "
                else:
                    row_str += " "
                j += 1
            result += row_str
            if i % 3 == 0:
                result += "\n\n"
            else:
                result += "\n"
            i += 1
        print(result)
        ###copied from logan to look pretty

    def is_solved(self):
        # TODO: Determine if the board has been correctly solved
        return self.board == self.solution


    def set(self, row, col, value):
        # TODO: Set this board's [row, col] cell to `value`
        if self.base[row][col] != "_":
            print("Whoops! That space can't be changed.")
        else:
            self.board[row][col] = value

    def solve_one(self):
        # TODO: Randomly fill in one correct answer on the board
        empty_cells = []
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == '_':
                    empty_cells.append((r, c))

        row, col = random.choice(empty_cells)
        self.set(row, col, self.solution[row][col])
        #what's this 'range'?

    def solve_all(self):
        # TODO: Complete the board
        self.board = self.solution


def get_difficulty():
    prompt = "What difficulty would you like to play? "
    valid_options = ["easy", "medium", "hard", "random"]

    print("Welcome to Sudoku!")
    print("Please choose: easy, medium, or hard")

    difficulty = input(prompt).lower()
    while difficulty not in valid_options:
        print("Invalid option! Try again.")
        difficulty = input(prompt).lower()
    return difficulty


def get_random_board(difficulty):
    all_boards = []
    for filename in os.listdir(difficulty):
        if not filename.endswith("_solved"):
            all_boards.append(filename)
    return difficulty + '/' + random.choice(all_boards)


# I'll explain this part in class, but basically this line means
# "when running this program, start here"
if __name__ == "__main__":
    # 1. Ask the user what difficulty they'd like to play
    difficulty = get_difficulty()

    # 2. Pick a random game board from that difficulty
    board_filename = get_random_board(difficulty)

    # 3. Parse the game board file into a list of lists
    game = SudokuGame(board_filename)

    # TODO
    # 4. Create the main game loop:
    #    while the board is not solved:
    #      - ask the user for their choice
    #      - update the game board
    while game.is_solved() == False:
        print("What would you like to do?")
        choice = input('> ')
        if choice == 'solve1':
            game.solve_one()
        elif choice == 'solveall':
            game.solve_all()
        else:
            row, col, value = choice.split(' ')
            row = int(row)
            col = int(col)
            game.set(row, col, value)
        print(game)



    # TODO
    # 5. End the game with a friendly message
    print("\n\n\nYou solved the board! Great job!\n")
    print(game)
