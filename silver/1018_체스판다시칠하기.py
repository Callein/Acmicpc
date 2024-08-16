"""
• 요소 하나씩 다 방문하면서 인접 요소 (상하좌우) 가 자신과 다른 색이면 +1.
• 8*8 로 잘랐을 때 그 합이 가장 큰쪽이 선택된 것.
•
•
•
"""

import sys

inputLine = sys.stdin.readline
N, M = map(int, inputLine().split())
board = [list(inputLine().strip()) for _ in range(N)]
score = [[0 for _ in range(M)] for _ in range(N)]

for n in range(N):
    for m in range(M):
        direction = []
        if n != 0:
            direction.append([-1,0])
        if n != N - 1:
            direction.append([1,0])
        if m != 0:
            direction.append([0,-1])
        if m != M - 1:
            direction.append([0,1])
        for dr, dc in direction:
            dn, dm = n + dr, m + dc
            if board[dn][dm] != board[n][m]:
                score[n][m] += 1



for s in score:
    print(s)