import os
##what is this?
import random

def parse_board(filename):
    # TODO: Parse a board filename into a list of lists
    f = open(board_filename)
    board = []
    for line in f.readlines():
        line = line.strip()
        row = line.split(' ')
        board.append(row)
    return board

class SudokuGame:
    # TODO: What other parameters should be passed to __init__?
    def __init__(self, board_filename):
        # TODO: What do we need to do within the __init__ body?
        self.board = parse_board(board_filename)
        self.solution = parse_board(board_filename + "_solved")
        print(self.solution)


def get_difficulty():
    # TODO: Ask the user what difficulty they'd like to play
    # If they respond with something invalid, keep asking
    #mine:
    #difficulty = raw_input("Pick a level: easy, medium or hard > ")
    #if difficulty != easy or medium or hard
    #    print("Pick again")
    prompt = "Pick a level: easy, medium, hard or random > "
    valid_options = ["easy", "medium", "hard", "random"]

    print("Welcome to sudoku!")

    difficulty = input(prompt).lower()
    while difficulty not in valid_options:
        print("Invalid option! Try again.")
        difficulty = input(prompt).lower()
    return difficulty


def get_random_board(difficulty):
    # TODO: Select a random board with the given difficulty
    # Hint: import random
    # Hint: How can you find all possible files in a directory?
    #mine:
    #if difficulty = easy
    #    board = open(filename)
    #    print(board.read())
    all_boards = []
    for filename in os.listdir(difficulty):
        if not filename.endswith("_solved"):
            all_boards.append(filename)
    return difficulty + '/' + random.choice(all_boards)
#what does listdir and endswith do?

# I'll explain this part in class, but basically this line means
# "when running this program, start here"
if __name__ == '__main__':
    # 1. Ask the user what difficulty they'd like to play
    difficulty = get_difficulty()

    # 2. Pick a random game board from that difficulty
    board_filename = get_random_board(difficulty)

    # 3. Parse the game board file into a list of lists
    game = SudokuGame(board_filename)
