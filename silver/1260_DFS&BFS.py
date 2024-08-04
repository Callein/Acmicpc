import sys
from collections import deque, defaultdict



N, M, start = map(int, sys.stdin.readline().split())
adj = defaultdict(list)
for _ in range(M):
    vertex, neighbour = map(int, sys.stdin.readline().split())
    adj[vertex].append(neighbour)
    # adj[neighbour].append(vertex)

dfs_result, bfs_result = graph_traversal(adj, N, start)
print("DFS:", " ".join(map(str, dfs_result)))
print("BFS:", " ".join(map(str, bfs_result)))
