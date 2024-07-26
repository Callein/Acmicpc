from collections import deque


def find_ripe_tomatoes(array):
    ripe_tomatoes = deque()
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == 1:
                ripe_tomatoes.append((i, j))
    return ripe_tomatoes


def is_all_ripe(array):
    for row in array:
        if 0 in row:
            return False
    return True


def bfs(cargo, N, M):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = find_ripe_tomatoes(cargo)
    days = -1

    while queue:
        for _ in range(len(queue)):
            row, col = queue.popleft()
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < N and 0 <= new_col < M and cargo[new_row][new_col] == 0:
                    cargo[new_row][new_col] = 1
                    queue.append((new_row, new_col))
        days += 1

    if is_all_ripe(cargo):
        return days
    else:
        return -1


M, N = map(int, input().split())
cargo = [list(map(int, input().strip().split())) for _ in range(N)]

result = bfs(cargo, N, M)
print(result)
