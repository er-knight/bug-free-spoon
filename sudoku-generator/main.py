import random

def valid(sudoku_grid, row, col, number):

    for _col in range(9):
        if sudoku_grid[row][_col] == number:
            return False 

    for _row in range(9):
        if sudoku_grid[_row][col] == number:
            return False

    corner_row = row - row % 3
    corner_col = col - col % 3

    for _row in range(3):
        for _col in range(3):
            if sudoku_grid[corner_row + _row][corner_col + _col] == number:
                return False

    return True
    
def solve(sudoku_grid, row=0, col=0):
    
    if col == 9:
        if row == 8:
            return True

        row += 1
        col = 0

    if sudoku_grid[row][col] > 0:
        return solve(sudoku_grid, row, col + 1)

    for number in random.sample(range(1, 10), k=9):
        if valid(sudoku_grid, row, col, number):
            sudoku_grid[row][col] = number

            if solve(sudoku_grid, row, col):
                return True

        sudoku_grid[row][col] = 0
    
    return False

def generate(sudoku_grid, k=40):
    # removes k numbers from sudoku_grid
    indices = random.sample(population=[(i, j) for i in range(9) for j in range(9)], k=k)

    solve(sudoku_grid)

    for row, col in indices:
        sudoku_grid[row][col] = 0
    

def formatted(sudoku_grid):
    for row in range(9):
        for col in range(9):
            if sudoku_grid[row][col] == 0:
                sudoku_grid[row][col] = " "

    return "\n".join([
        f"╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗",
        f"║ {sudoku_grid[0][0]} │ {sudoku_grid[0][1]} │ {sudoku_grid[0][2]} ║ {sudoku_grid[0][3]} │ {sudoku_grid[0][4]} │ {sudoku_grid[0][5]} ║ {sudoku_grid[0][6]} │ {sudoku_grid[0][7]} │ {sudoku_grid[0][8]} ║",
        f"╟───┼───┼───╫───┼───┼───╫───┼───┼───╢",
        f"║ {sudoku_grid[1][0]} │ {sudoku_grid[1][1]} │ {sudoku_grid[1][2]} ║ {sudoku_grid[1][3]} │ {sudoku_grid[1][4]} │ {sudoku_grid[1][5]} ║ {sudoku_grid[1][6]} │ {sudoku_grid[1][7]} │ {sudoku_grid[1][8]} ║",
        f"╟───┼───┼───╫───┼───┼───╫───┼───┼───╢",
        f"║ {sudoku_grid[2][0]} │ {sudoku_grid[2][1]} │ {sudoku_grid[2][2]} ║ {sudoku_grid[2][3]} │ {sudoku_grid[2][4]} │ {sudoku_grid[2][5]} ║ {sudoku_grid[2][6]} │ {sudoku_grid[2][7]} │ {sudoku_grid[2][8]} ║",
        f"╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣",
        f"║ {sudoku_grid[3][0]} │ {sudoku_grid[3][1]} │ {sudoku_grid[3][2]} ║ {sudoku_grid[3][3]} │ {sudoku_grid[3][4]} │ {sudoku_grid[3][5]} ║ {sudoku_grid[3][6]} │ {sudoku_grid[3][7]} │ {sudoku_grid[3][8]} ║",
        f"╟───┼───┼───╫───┼───┼───╫───┼───┼───╢",
        f"║ {sudoku_grid[4][0]} │ {sudoku_grid[4][1]} │ {sudoku_grid[4][2]} ║ {sudoku_grid[4][3]} │ {sudoku_grid[4][4]} │ {sudoku_grid[4][5]} ║ {sudoku_grid[4][6]} │ {sudoku_grid[4][7]} │ {sudoku_grid[4][8]} ║",
        f"╟───┼───┼───╫───┼───┼───╫───┼───┼───╢",
        f"║ {sudoku_grid[5][0]} │ {sudoku_grid[5][1]} │ {sudoku_grid[5][2]} ║ {sudoku_grid[5][3]} │ {sudoku_grid[5][4]} │ {sudoku_grid[5][5]} ║ {sudoku_grid[5][6]} │ {sudoku_grid[5][7]} │ {sudoku_grid[5][8]} ║",
        f"╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣",
        f"║ {sudoku_grid[6][0]} │ {sudoku_grid[6][1]} │ {sudoku_grid[6][2]} ║ {sudoku_grid[6][3]} │ {sudoku_grid[6][4]} │ {sudoku_grid[6][5]} ║ {sudoku_grid[6][6]} │ {sudoku_grid[6][7]} │ {sudoku_grid[6][8]} ║",
        f"╟───┼───┼───╫───┼───┼───╫───┼───┼───╢",
        f"║ {sudoku_grid[7][0]} │ {sudoku_grid[7][1]} │ {sudoku_grid[7][2]} ║ {sudoku_grid[7][3]} │ {sudoku_grid[7][4]} │ {sudoku_grid[7][5]} ║ {sudoku_grid[7][6]} │ {sudoku_grid[7][7]} │ {sudoku_grid[7][8]} ║",
        f"╟───┼───┼───╫───┼───┼───╫───┼───┼───╢",
        f"║ {sudoku_grid[8][0]} │ {sudoku_grid[8][1]} │ {sudoku_grid[8][2]} ║ {sudoku_grid[8][3]} │ {sudoku_grid[8][4]} │ {sudoku_grid[8][5]} ║ {sudoku_grid[8][6]} │ {sudoku_grid[8][7]} │ {sudoku_grid[8][8]} ║",
        f"╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝"
    ])

if __name__ == "__main__":

    sudoku_grid = [[0 for j in range(1, 10)] for i in range(9)]

    generate(sudoku_grid)

    print(formatted(sudoku_grid))

# output.txt
# ╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗
# ║ 1 │ 3 │ 7 ║   │   │   ║ 9 │   │   ║
# ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
# ║   │ 5 │   ║ 2 │ 1 │   ║   │   │ 7 ║
# ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
# ║ 2 │   │   ║   │ 8 │ 3 ║   │   │ 1 ║
# ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
# ║ 3 │   │ 9 ║   │ 7 │ 6 ║ 4 │   │   ║
# ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
# ║   │   │ 5 ║   │ 3 │   ║ 7 │ 2 │ 9 ║
# ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
# ║   │   │ 1 ║   │ 9 │   ║ 6 │   │   ║
# ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
# ║ 7 │ 6 │ 2 ║ 3 │ 5 │ 8 ║   │ 9 │   ║
# ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
# ║   │   │ 3 ║ 4 │ 2 │   ║   │   │   ║
# ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
# ║ 5 │ 4 │ 8 ║ 9 │   │   ║   │ 7 │ 3 ║
# ╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝

# python3 main.py > output.txt

# sudoku generator : https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python
