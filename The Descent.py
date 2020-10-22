import sys
import math

#   Problem: https://www.codingame.com/ide/puzzle/the-descent
#   Autor: Dawid Szabłowski s16667

# game loop
while True:
    mountainIndex = 0
    highest = 0
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        if(mountain_h > highest):
            highest = mountain_h
            print(highest, file=sys.stderr, flush=True)
            shoot = mountainIndex
        mountainIndex = mountainIndex+1
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # The index of the mountain to fire on.
    print(shoot)