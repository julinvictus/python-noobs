import os
import random
import time

# Seconds penalty for each solve
PENALTY_TIME = 30

VALID_DIFFICULTIES = ["easy", "medium", "hard"]
EASY_HIGHSCORE_FILENAME = "easy.highscores"
MEDIUM_HIGHSCORE_FILENAME = "medium.highscores"
HARD_HIGHSCORE_FILENAME = "hard.highscores"
NUM_HIGHSCORES = 10

RED = "\033[0;31m"
GREEN = "\033[0;32m"
RESET = "\033[0m"

def red(s):
    # TODO: Make sure `s` is a string!
    assert isinstance(s, str)
    return RED + s + RESET


def green(s):
    # TODO: Make sure `s` is a string!
    assert isinstance(s, str)
    return GREEN + s + RESET


def parse_board(filename):
    # TODO: Make sure `filename` is a string!
    assert isinstance(filename, str)
    f = open(filename)
    board = []
    for line in f.readlines():
        line = line.strip()
        row = line.split(" ")
        board.append(row)
    # TODO: Make sure `board` is 9 x 9
    assert len(board) == 9
    return board


def get_timer_string(elapsed_time):
    # TODO: Make sure `elapsed_time` is an int or float
    # TODO: Write this function that takes a number representing the elapsed
    #       time in seconds and returns a human-readable formatted string.
    # Example: input = 230.4 => output = "3min 50.4sec"
    assert isinstance(elapsed_time, (int, float))

    seconds_in_minute = 60
    seconds_in_hour = seconds_in_minute * 60
    hours = int(elapsed_time / seconds_in_hour)
    elapsed_time = elapsed_time % seconds_in_hour

    minutes = int(elapsed_time / seconds_in_minute)
    elapsed_time = elapsed_time % seconds_in_minute

    seconds = round(elapsed_time, 1)

    result = ""
    if hours > 0:
        result += str(hours) + "hr "
    if minutes > 0:
        result += str(minutes) + "min "
    result += str(seconds) + "sec"
    return result


def get_high_scores(difficulty):
    # TODO: Make sure `difficulty` is a valid option
    # TODO: Write this function that takes a difficulty and returns the top
    #       highscores for that difficulty by reading the highscores file.
    # The highscores file should be in the following format:
    # name|elapsed_in_seconds
    # name2|elapsed_in_seconds
    # etc.
    assert isinstance(difficulty, str)
    assert difficulty in VALID_DIFFICULTIES

    if difficulty == "easy":
        fn = EASY_HIGHSCORE_FILENAME
    elif difficulty == "medium":
        fn = MEDIUM_HIGHSCORE_FILENAME
    else:
        fn = HARD_HIGHSCORE_FILENAME

    # Easy way to assure the file exists
    open(fn, "a").close()
    f = open(fn)

    high_scores = []
    for line in f.readlines():
        line = line.strip()
        name, elapsed = line.split("|")
        high_scores.append((name, elapsed))

    f.close()
    return high_scores


def write_high_scores(difficulty, names_with_scores):
    # TODO: Make sure `difficulty` is a valid option
    # TODO: Make sure `names_with_scores` is a list
    # TODO: Make sure `names_with_scores` has at most `NUM_HIGHSCORES` elements
    # TODO: Write this function that takes a difficulty and a list of
    #       (name, score) pairs and writes to the correct highscores file
    assert isinstance(difficulty, str)
    assert difficulty in VALID_DIFFICULTIES
    assert isinstance(names_with_scores, list)


    if difficulty == "easy":
        fn = EASY_HIGHSCORE_FILENAME
    elif difficulty == "medium":
        fn = MEDIUM_HIGHSCORE_FILENAME
    else:
        fn = HARD_HIGHSCORE_FILENAME
    f = open(fn, "w")

    for (name, elapsed) in names_with_scores:
        line = str(name) + "|" + str(elapsed) + "\n"
        f.write(line)
    f.close()



def print_high_scores(high_scores):
    # TODO: Make sure `high_scores` is a list
    # TODO: Write this function that prints the highscores in a convenient
    #       format that is easy to read
    assert isinstance(high_scores, list)

    position = 1
    for (name, elapsed) in high_scores:
        elapsed_str = get_timer_string(elapsed)
        print("%2d %15s %12s" % (position, name, elapsed_str))
        position += 1


class SudokuGame:
    def __init__(self, board_filename):
        # TODO: Make sure `board_filename` is a string!
        assert isinstance(board_filename, str)
        self.base = parse_board(board_filename)
        self.board = parse_board(board_filename)
        self.solution = parse_board(board_filename + "_solved")

    def __str__(self):
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

    def is_solved(self):
        return self.board == self.solution

    def set(self, row, col, value):
        # TODO: Make sure row and col are ints
        # TODO: Make sure value is a string
        # TODO: Make sure row and col are both between [0, 8]
        assert isinstance(row, int)
        assert isinstance(col, int)
        assert isinstance(value, str)
        assert row >= 0 and row <= 8
        assert col >= 0 and row <= 8
        if self.base[row][col] != "_":
            print("Whoops! That space can't be changed.")
        else:
            self.board[row][col] = value

    def solve_one(self):
        empty_cells = []
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == '_':
                    empty_cells.append((r, c))

        # TODO: Make sure there is at least one empty cell
        assert len(empty_cells) > 0
        row, col = random.choice(empty_cells)
        self.set(row, col, self.solution[row][col])

    def solve_all(self):
        self.board = self.solution


def get_difficulty():
    prompt = "What difficulty would you like to play? "
    valid_options = ["easy", "medium", "hard", "random"]

    print("******************")
    print("Welcome to Sudoku!")
    print("******************")
    print("Please choose: easy, medium, or hard\n")

    difficulty = input(prompt).lower()
    while difficulty not in valid_options:
        print("Invalid option! Try again.")
        difficulty = input(prompt).lower()
    return difficulty


def get_random_board(difficulty):
    # TODO: Make sure `difficulty` is a valid option
    assert difficulty in VALID_DIFFICULTIES

    all_boards = []
    for filename in os.listdir(difficulty):
        if not filename.endswith("_solved"):
            all_boards.append(filename)
    # TODO: Make sure there is at least one board available
    return difficulty + "/" + random.choice(all_boards)


def choice_is_valid(choice):
    # TODO: Make sure `choice` is a string
    assert isinstance(choice, str)
    choice  = choice.strip(" ")
    valid_options = ["solve1", "solveall", "check"]

    # This is a "set" choice if there are two spaces in the string
    if choice.count(" ") == 2 or choice in valid_options:
        return True
    return False


def get_choice():
    options_str = "Choose an option: solve1, solveall or check"
    print(options_str)
    choice = input("> ")
    while not choice_is_valid(choice):
        print("That's not a valid choice!")
        print(options_str)
        choice = input("> ")
    return choice


# I'll explain this part in class, but basically this line means
# "when running this program, start here"
if __name__ == "__main__":
    # 1. Ask the user what difficulty they'd like to play
    difficulty = get_difficulty()

    # 2. Pick a random game board from that difficulty
    board_filename = get_random_board(difficulty)

    # 3. Parse the game board file into a list of lists
    game = SudokuGame(board_filename)
    choice = None

    # TODO: Start a timer (HINT: import time)
    start = time.time()
    penalty_time = 0

    # 4. The main game loop
    while not game.is_solved():
        # Print one empty line before the game board
        if choice != "check":
            print()
            print(game)

        choice = get_choice()
        if choice == "solve1":
            game.solve_one()
        elif choice == "solveall":
            game.solve_all()
        elif choice == "check":
            print()
            game.check()
        else:
            # input is of the form `row col value`
            row, col, value = choice.split(" ")
            # we subtract one so we can use 1-indexing
            row = int(row) - 1
            col = int(col) - 1
            game.set(row, col, value)

    # 5. End the game with a friendly message
    print("\n\n\nYou solved the board! Great job!\n")
    print(game)

    # TODO: Print the elapsed time
    elapsed = time.time() - start
    elapsed_str = get_timer_string(elapsed)
    print("You solved this board in %s" % elapsed_str)

    # TODO: If the user is in the top NUM_HIGHSCORES scores for this difficulty,
    #       prompt for his/her name and add them to the high scores list
    # HINT: Look at the helpers `get_high_scores` and `write_high_scores`
    high_scores = get_high_scores(difficulty)

    slowest = elapsed + 1
    if len(high_scores) > 0:
        name_of_slowest, slowest = high_scores[-1]
        slowest = float(slowest)

    if elapsed < slowest or len(high_scores) < NUM_HIGHSCORES:
        # The player got a new highscore!
        print("New high score!")
        print("Please input your name for the high scores list")
        player_name = input("> ")

        new_high_scores = []

        added_yet = False
        for (name, timer) in high_scores:
            timer = float(timer)
            if elapsed < timer and not added_yet:
                new_high_scores.append((player_name, elapsed))
                added_yet = True
            new_high_scores.append((name, timer))

        # Add the name to the end (in case we don't have NUM_HIGHSCORES yet)
        if not added_yet:
            new_high_scores.append((player_name, elapsed))

        # Make sure we don't send too many high scores to the list
        new_high_scores = new_high_scores[:NUM_HIGHSCORES]

        write_high_scores(difficulty, new_high_scores)
        print_high_scores(new_high_scores)
