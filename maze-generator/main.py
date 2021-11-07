# # https://people.cs.ksu.edu/~ashley78/wiki.ashleycoleman.me/index.php/Eller's_Algorithm.html
# # https://weblog.jamisbuck.org/2010/12/29/maze-generation-eller-s-algorithm
# # http://www.neocomputer.org/projects/eller.html
# # https://clarkcoding.com/eller.html
# # https://en.wikipedia.org/wiki/Maze_generation_algorithm
# # https://youtu.be/sVcB8vUFlmU (8 Maze Generating Algorithms in 3 Minutes)
# # https://en.wikipedia.org/wiki/Maze-solving_algorithm


# # https://gist.github.com/jamis/761534

# import random
# import time

# width  = 5
# height = 5 
# # seed   = random.seed(0xFFFF_FFFF)

# N, S, E, W = 1, 2, 4, 8
# DX         = { E : 1, W : -1, N :  0, S : 0 }
# DY         = { E : 0, W :  0, N : -1, S : 1 }
# OPPOSITE   = { E : W, W :  E, N :  S, S : N }

# grid = [[0 for _ in range(width)] for _ in range(height)]

# def display_maze(grid):
#     print(" " + "_" * (len(grid[0]) * 2 - 1))
#     for y, row in enumerate(grid):
#         print("|", end="")
#         for x, cell in enumerate(row):
#             if cell == 0 and (y + 1) < len(grid) and grid[y + 1][x] == 0:
#                 print(" ", end="")
#             else:
#                 print(" " if (cell & S != 0) else "_", end="")

#             if cell == 0 and (x + 1) < len(row) and row[x + 1] == 0:
#                 print(" " if ((y + 1) < len(grid) and (grid[y + 1][x] == 0 or grid[y + 1][x + 1] == 0)) else "_", end="")
#             elif cell & E != 0:
#                 print(" " if ((cell | row[x + 1]) & S != 0) else "_", end="")
#             else:
#                 print("|", end="")

#         print()

# for y in range(height):
#     for x in range(width):
#         # time.sleep(0.02)

#         dirs = []

#         if y > 0: dirs.append(N)
#         if x > 0: dirs.append(W)

#         if dirs: # len(dirs) > 0
#             dir_ = random.choice(dirs)

#             nx, ny        = x + DX[dir_], y + DY[dir_]
#             grid[y][x]   |= dir_
#             grid[ny][nx] |= OPPOSITE[dir_]

# display_maze(grid)
