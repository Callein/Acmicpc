"""
M * N 이중 배열으로 받는다.
하나씩 들여다보면서 움직이는데, 익은 놈이면, 인접 (상,하,좌,우) 토마토를 익힌다.
만약 하루가 지났는데도 (loop 한번 지났는데도) 배열이 일치한다? 그러면 escape 한다.
"""

import sys
from copy import deepcopy


def find_tomato(array, val):
    indices = []
    for i, row in enumerate(array):
        for j, element in enumerate(row):
            if element == val:
                indices.append((i, j))
    return indices


M, N = map(int, sys.stdin.readline().split())
cargo = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
day, resume = 0, True

print(cargo)

while resume:
    tmp = deepcopy(cargo)
    ripe_tomatoes = find_tomato(cargo,1)
    print("익은 토마토 :", ripe_tomatoes)
    for row, col in ripe_tomatoes:
        print(row, col)
        if row > 0:
            if cargo[row-1][col] == 0:
                cargo[row-1][col] = 1
        if row < N - 1:
            if cargo[row+1][col] == 0:
                cargo[row+1][col] = 1
        if col > 0:
            if cargo[row][col-1] == 0:
                cargo[row][col-1] = 1
        if col < M - 1:
            if cargo[row][col+1] == 0:
                cargo[row][col+1] = 1
    print(cargo)
    print(tmp)
    if cargo == tmp:
        resume = False
        if len(find_tomato(cargo, 0)) != 0:
            day = -1
    else:
        day += 1

print(day)
