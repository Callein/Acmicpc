"""
n 개 - 이동시 필요한 횟수
1 - 1
2 - 3
3 - 7
4 - 15
5 - 31

원판의 개수를 n, 이 때 3번 rod 로 이동하기 위한 횟수를 T(n) 이라고 했을 때,
T(n) = 1 , if n = 1
T(n+1) = 2*T(n) + 1

1. n-1 개의 원판을 2번 rod 로 이동
2. n 번째 원판을 3번 rod 로 이동
3. n-1 개의 원판을 2번 rod 에서 3번 rod 로 이동
"""

import sys
from collections import deque


def move(n, from_rod, to_rod, aux_rod, moves):
    if n == 1:
        moves.append((from_rod, to_rod))
        return
    # 1. n-1 개의 원판을 2번 rod 로 이동
    move(n - 1, from_rod, aux_rod, to_rod, moves)
    # 2. n 번째 원판을 3번 rod 로 이동
    moves.append((from_rod, to_rod))
    # 3. n-1 개의 원판을 2번 rod 에서 3번 rod 로 이동
    move(n - 1, aux_rod, to_rod, from_rod, moves)


def hanoi(n):
    moves = deque()
    move(n, 1, 3, 2, moves)
    return moves


n = int(sys.stdin.readline())
moves = hanoi(n)

print(len(moves))
for move in moves:
    print(move[0], move[1])
