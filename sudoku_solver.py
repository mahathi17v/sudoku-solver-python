grid = []

print("Enter Sudoku rows (use 0 for empty cells)")
print("Example: 9 0 6 0 7 0 4 0 3\n")

for i in range(9):
    row = list(map(int, input(f"Row {i + 1}: ").split()))

    while len(row) != 9:
        print("Please enter exactly 9 numbers.")
        row = list(map(int, input(f"Row {i + 1}: ").split()))

    grid.append(row)


def print_grid():
    print("\nSolved Sudoku:\n")

    for row in grid:
        print(*row)


def possible(row, col, num):

    # Check row
    for i in range(9):
        if grid[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True


def solve():

    for row in range(9):
        for col in range(9):

            if grid[row][col] == 0:

                for num in range(1, 10):

                    if possible(row, col, num):

                        grid[row][col] = num

                        if solve():
                            return True

                        grid[row][col] = 0

                return False

    return True


if solve():
    print_grid()
else:
    print("\nNo solution exists.")