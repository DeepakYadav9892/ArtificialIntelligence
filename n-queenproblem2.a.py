N = 4  # Number of queens and size of the chess board (4x4)

# Function to print the solution board
def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

# Utility function to check if placing a queen at (row, col) is safe
def isSafe(board, row, col):
    # Check the row on the left
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

# Recursive function to solve N Queen problem
def solveNQUtil(board, col):
    # Base Case: If all queens are placed
    if col >= N:
        return True

    # Try placing queen in all rows one by one
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1  # Place queen

            # Recur to place rest of the queens
            if solveNQUtil(board, col + 1):
                return True

            board[i][col] = 0  # Backtrack if placing queen doesn't lead to solution

    return False  # No place found in this column

# Main function
def solveNQ():
    board = [[0] * N for _ in range(N)]  # Create 4x4 board with all 0

    if not solveNQUtil(board, 0):
        print("Solution does not exist")
        return False

    printSolution(board)
    return True

# Run the N-Queens solution
solveNQ()
