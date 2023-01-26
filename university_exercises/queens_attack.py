"""In the game of chess, a queen can attack pieces which are on the
    same row, column, or diagonal. A chessboard can be represented
    by an 8 by 8 array. A 1 in the array represents a queen on the
    corresponding square, and a O in the array represents an unoccupied square.
    Your program is to read the location of two queens and then update the
    array appropriately.
    Then process the board and indicate whether or not the two queens are
    positioned so that they attack each other.
    """


class QueenAttack:
    def __init__(self, board):
        self.board = board
        self.queen_positions = []

    def reset_game(self):
        self.queen_positions = []
        self.board = [[0 for x in y] for y in self.board]

    def place_queen(self, row, col):
        if row < 0 or 8 < row or col < 0 or 8 < col:
            raise ValueError("Invalid indexes")

        if len(self.queen_positions) == 2:
            raise ValueError("There are already two Queens on the board")

        if len(self.queen_positions) == 1:
            first_queen = self.queen_positions[0]
            if first_queen == (row, col):
                raise ValueError("There is already a Queen at that position")

        self.queen_positions.append([row, col])
        self.board[row][col] = 1

    def print_board(self):
        print()
        print("Printing board...")
        for row in self.board:
            for tile in row:
                print(tile, end="  ")
            print()
        print()

    def check_board(self):
        if q.are_queens_safe():
            print("The Queens are safe from each other")
        else:
            print("The Queens are not safe from each other!")

    def copy_queen_position(self, queen):
        return [queen[0], queen[1]]

    def are_queens_safe(self):
        queen_a = self.queen_positions[0]
        queen_b = self.queen_positions[1]
        # check vertical and horizontal
        if queen_a[0] == queen_b[0] or queen_a[1] == queen_b[1]:
            return False
        # check upper left
        temp = self.copy_queen_position(queen_a)
        while temp[0] >= 0 and temp[1] >= 0:
            temp[0] -= 1
            temp[1] -= 1
            if temp == queen_b:
                return False
        # check upper right
        temp = self.copy_queen_position(queen_a)
        while temp[0] >= 0 and temp[1] < len(self.board):
            temp[0] -= 1
            temp[1] += 1
            if temp == queen_b:
                return False
        # check lower left
        temp = self.copy_queen_position(queen_a)
        while temp[0] < len(self.board) and temp[1] >= 0:
            temp[0] += 1
            temp[1] -= 1
            if temp == queen_b:
                return False
        # check lower right
        temp = self.copy_queen_position(queen_a)
        while temp[0] < len(self.board) and temp[1] < len(self.board):
            temp[0] += 1
            temp[1] += 1
            if temp == queen_b:
                return False
        # if no matches the queens are safe from each other
        return True


# testing code
chessboard = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

# should be false
q = QueenAttack(chessboard)
try:
    q.place_queen(2, 5)
    q.place_queen(7, 0)
except ValueError as e:
    print(e)
q.print_board()
q.check_board()

q.reset_game()

# should be true
try:
    q.place_queen(2, 5)
    q.place_queen(7, 1)
except ValueError as e:
    print(e)
q.print_board()
q.check_board()
