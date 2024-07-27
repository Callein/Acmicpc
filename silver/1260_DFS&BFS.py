import sys
from collections import deque, defaultdict


def DFS(adj, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            for neighbour in sorted(adj[vertex], reverse=True):
                if neighbour not in visited:
                    stack.append(neighbour)

    return result

def BFS(adj, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            for neighbour in sorted(adj[vertex]):
                if neighbour not in visited:
                    queue.append(neighbour)

    return result



def graph_traversal(adj, N, start):
    visited = set()
    dfs_result = DFS(adj, start)
    visited.update(dfs_result)

    bfs_result = BFS(adj, start)
    visited.update(bfs_result)

    for node in range(1, N + 1):
        if node not in visited:
            dfs_result.extend(DFS(adj, node))
            bfs_result.extend(BFS(adj, node))
            visited.add(node)

    return dfs_result, bfs_result


N, M, start = map(int, sys.stdin.readline().split())
adj = defaultdict(list)
for _ in range(M):
    vertex, neighbour = map(int, sys.stdin.readline().split())
    adj[vertex].append(neighbour)
    # adj[neighbour].append(vertex)

dfs_result, bfs_result = graph_traversal(adj, N, start)
print("DFS:", " ".join(map(str, dfs_result)))
print("BFS:", " ".join(map(str, bfs_result)))
