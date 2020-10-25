import sys
import math

#   Problem: https://www.codingame.com/ide/puzzle/shadows-of-the-knight-episode-1
#   Autor: Dawid Szabłowski s16667

w, h = [int(i) for i in input().split()]
n = int(input())
x0, y0 = [int(i) for i in input().split()]

top = 0
bottom = h
left = 0
right = w
jumpX = x0
jumpY = y0
lastMoveY = ""
lastMoveX = ""

while True:
    bomb_dir = input()

    if (lastMoveY == "D" and "D" in bomb_dir):
        top = jumpY
    if (lastMoveY == "U" and "U" in bomb_dir):
        bottom = jumpY
    if (lastMoveY == "D" and "U" in bomb_dir):
        bottom = jumpY
    if (lastMoveY == "U" and "D" in bomb_dir):
        top = jumpY
    if (lastMoveX == "R" and "R" in bomb_dir):
        left = jumpX
    if (lastMoveX == "L" and "L" in bomb_dir):
        right = jumpX
    if (lastMoveX == "L" and "R" in bomb_dir):
        left = jumpX
    if (lastMoveX == "R" and "L" in bomb_dir):
        right = jumpX

    if ("D" in bomb_dir):
        jumpY = (bottom + top) // 2
        lastMoveY = "D"

    if ("U" in bomb_dir):
        jumpY = (bottom + top) // 2
        lastMoveY = "D"

    if ("R" in bomb_dir):
        jumpX = (left + right) // 2
        lastMoveX = "R"

    if ("L" in bomb_dir):
        jumpX = (left + right) // 2
        lastMoveX = "L"

    print(jumpX, jumpY)
