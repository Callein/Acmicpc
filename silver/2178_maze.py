"""
1. 처음에 모든 지점까지의 거리를 무한대로 설정.
2. 시작점부터 시작하여 네 방향으로 이동 가능한 지점을 탐색.
3. 이동 가능한 지점에 대해 현재까지의 최단 거리를 갱신하고, 갱신된 거리와 지점을 우선순위 큐에 추가.
4. 큐에서 가장 짧은 거리를 가진 지점을 꺼내어 같은 과정을 반복.
5. 도착점에 도달하면 그때의 거리를 반환.
6. 큐가 빌 때까지 도착점에 도달하지 못하면 -1을 반환.

-> 가중치가 1인 다익스트라를 이용했지만, 사실 deque를 사용한 BFS로도 풀 수 있다.
"""

import heapq
import sys


def dijkstra_maze(N, M, maze):
    distances = [[float('inf')] * M for _ in range(N)]
    distances[0][0] = 1
    # (거리, 행, 열)
    priority_queue = [(1, 0, 0)]
    # 상, 하, 좌, 우 이동
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while priority_queue:
        current_distance, row, col = heapq.heappop(priority_queue)

        # 현재 위치가 도착점이라면 종료
        if row == N - 1 and col == M - 1:
            return current_distance

        # 방향 설정
        for dr, dc in directions:
            # 새 위치 선정
            new_row, new_col = row + dr, col + dc

            # 생성한 위치가 미로를 벗어나지 않는다면 진행.
            if 0 <= new_row < N and 0 <= new_col < M and maze[new_row][new_col] == 1:
                new_distance = current_distance + 1
                #  현 경로가 해당 위치의 최단거리라면, distance 최신화 후 큐에 추가.
                if new_distance < distances[new_row][new_col]:
                    distances[new_row][new_col] = new_distance
                    heapq.heappush(priority_queue, (new_distance, new_row, new_col))

    return -1


input = sys.stdin.readline
N, M = map(int, input().split(' '))
maze = [list(map(int, list(input().strip()))) for _ in range(N)]

print(dijkstra_maze(N, M, maze))
