import random
import math

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def print_board(matrix, player, monsters):
    for i, point_ in enumerate(matrix):
        if point_ in monsters:
            print("M", end=" ")
        elif point_ == player:
            print("P", end=" ")
        else:
            print("-", end=" ")

        if (i + 1) % 5 == 0: print()

def print_distance(player, monsters):
    for i, monster in enumerate(monsters, start=1):
        print(f"monster {i} is {math.sqrt(abs(monster.x - player.x) + abs(monster.y - player.y)):.5f} away.")

n = 5

matrix = [point(i, j) for i in range(n) for j in range(n)]

player = matrix[0]
finish = matrix[-1]

monsters = random.sample(matrix[1:-1], k=n)
# monsters can be anywhere except start and finish

print_board(matrix, player, monsters)

print_distance(player, monsters)