import sys
import math

#   Problem: https://www.codingame.com/ide/puzzle/power-of-thor-episode-1
#   Autor: Dawid Szabłowski s16667

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    move_x = initial_tx - light_x
    move_y = initial_ty - light_y

    if (move_x > 0) and (move_y > 0):
        if (move_x > move_y):
            move_max = move_y
        else:
            move_max = move_x
        for x in range(0, move_max):
            print("NW")

    if (move_x < 0) and (move_y < 0):
        move_diagonal1 = math.sqrt(move_x * move_x)
        move_diagonal1 = int(move_diagonal1)
        move_diagonal2 = math.sqrt(move_y * move_y)
        move_diagonal2 = int(move_diagonal2)
        if (move_diagonal1 > move_diagonal2):
            move_max = move_diagonal2
        else:
            move_max = move_diagonal1
        for x in range(0, move_max):
            print("SE")

    if (move_x < 0) and (move_y > 0):
        move_diagonal1 = math.sqrt(move_x * move_x)
        move_diagonal1 = int(move_diagonal1)
        if (move_diagonal1 > move_y):
            move_max = move_y
        else:
            move_max = move_diagonal1
        for x in range(0, move_max):
            print("NE")

    if (move_x > 0) and (move_y < 0):
        move_diagonal2 = math.sqrt(move_y * move_y)
        move_diagonal2 = int(move_diagonal2)
        if (move_x > move_diagonal2):
            move_max = move_diagonal2
        else:
            move_max = move_x
        for x in range(0, move_max):
            print("SW")

    if (move_x > 0):
        for x in range(0, move_x):
            print("W")
    if (move_x < 0):
        move_x = math.sqrt(move_x * move_x)
        move_x = int(move_x)
        for x in range(0, move_x):
            print("E")

    if (move_y > 0):
        for x in range(0, move_y):
            print("N")
    if (move_y < 0):
        move_y = math.sqrt(move_y * move_y)
        move_y = int(move_y)
        for x in range(0, move_y):
            print("S")
