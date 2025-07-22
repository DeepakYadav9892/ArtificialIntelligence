# N-Queens Problem Solution for N = 4 using Backtracking

N = 4  # Size of the board and number of queens

# Function to print the board
def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

# Function to check if placing a queen at board[row][col] is safe
def isSafe(board, row, col):
    # Check this row on the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower-left diagonal
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# Recursive function to solve N-Queens problem
def solveNQUtil(board, col):
    # Base case: If all queens are placed
    if col >= N:
        return True

    # Try placing this queen in all rows one by one
    for i in range(N):
        if isSafe(board, i, col):
            # Place the queen
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solveNQUtil(board, col + 1):
                return True

            # If placing queen doesn't lead to a solution, BACKTRACK
            board[i][col] = 0

    # If queen cannot be placed in any row in this column
    return False

# Main function to solve the N-Queens problem
def solveNQ():
    # Create a 4x4 board initialized with 0
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Solve using backtracking
    if not solveNQUtil(board, 0):
        print("Solution does not exist")
        return False

    # If solution exists, print it
    print("One of the valid solutions:")
    printSolution(board)
    return True

# Run the N-Queens solver
solveNQ()
