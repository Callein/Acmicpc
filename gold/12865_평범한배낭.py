import sys
import heapq

"""
Fractional 이 아니기 때문에 Greedy 가 아닌 Brute Force, DP, Branch and Bound 로 접근해야 함.

[Branch and Bound]
• Item 을 B/K (무게당 가치) 가 큰 순으로 정렬
• Bound = 현재 까지 benefit + 넣을 수 있을 만큼 (weight overflow 하지 않을 만큼) 넣었을 때 benefit
             + 남은 것중 B/K 가 최대인 것을 남은 공간에 잘라 넣었을 때의 benefit
• max_benefit = max(max_benefit, benefit)
• promising : bound > max_benefit 이고 weight <= K 일 때.
• non-promising : bound <= max_benefit 이거나 weight > K 일 때.
    • weight <= W 일 때 해당 node 에서 계산된 benefit 은 유효하다.
    • weight > W 일 때는 해당 node 에서 계산된 benefit 이 무효하다. max_benefit 이 update 되서는 안된다.
• Promising 인 node 가 없을 때 까지 BFS 검색 시행.

<B&B 반례>
4 6
6 13
3 8
7 15
2 6

출력  : 13
기대값 : 14 ( 8+6 ) 

"""


class Item:
    def __init__(self, weight, benefit):
        self.weight = weight
        self.benefit = benefit
        self.benefit_per_weight = benefit / weight


class Node:
    def __init__(self, index, curr_benefit, curr_weight, max_weight, items):
        self.index = index
        self.curr_benefit = curr_benefit
        self.curr_weight = curr_weight
        self.bound = estimate_bound(curr_benefit, curr_weight, max_weight, index, items)

    def __lt__(self, other):
        return self.bound > other.bound


def estimate_bound(curr_benefit, curr_weight, max_weight, index, items):
    if curr_weight > max_weight:
        return 0
    bound = curr_benefit
    total_weight = curr_weight
    while index < len(items) and total_weight + items[index].weight <= max_weight:
        total_weight += items[index].weight
        bound += items[index].benefit
        index += 1
    if index < len(items):
        bound += (max_weight - total_weight) * items[index].benefit_per_weight
    return bound


N, K = map(int, sys.stdin.readline().split())

# Item 정보 입력 및 정렬
items = []
for _ in range(N):
    w, v = map(int, sys.stdin.readline().split())
    items.append(Item(w, v))
items = sorted(items, key=lambda item: item.benefit_per_weight)


promising = []
max_benefit = 0
curr_benefit = 0
curr_weight = 0
curr_index = 0

# 첫 노드
node = Node(-1, 0, 0, K, items)
heapq.heappush(promising, node)

while len(promising) > 0:
    curr_node = heapq.heappop(promising)
    curr_benefit = curr_node.curr_benefit
    curr_weight = curr_node.curr_weight
    curr_index = curr_node.index + 1
    max_benefit = max(max_benefit, curr_node.curr_benefit)
    print("c_b c_w m_b c_i")
    print(curr_benefit, curr_weight, max_benefit, curr_index)
    if curr_index < len(items):
        # 넣을때
        node1 = Node(curr_index, curr_benefit + items[curr_index].benefit, curr_weight + items[curr_index].weight, K, items)
        print(node1.curr_benefit, node1.curr_weight, round(node1.bound,1), node1.index)
        if node1.bound >= max_benefit and node1.curr_weight < K:
            heapq.heappush(promising, node1)
            print("프로미싱")
        elif node1.curr_weight <= K:
            print("맥스 갱신")
            max_benefit = max(max_benefit, node1.curr_benefit)
        # 안넣을 때
        node2 = Node(curr_index, curr_benefit, curr_weight, K, items)
        print(node2.curr_benefit, node2.curr_weight, round(node2.bound,1), node2.index)
        if node2.bound >= max_benefit and node2.curr_weight < K:
            heapq.heappush(promising, node2)
            print("프로미싱")
        elif node2.curr_weight <= K:
            print("맥스 갱신")
            max_benefit = max(max_benefit, node2.curr_benefit)
    print()
print(max_benefit)

for i in items:
    print(i.weight, i.benefit, i.benefit_per_weight)


# [DP]
def knapsack_dp():
    n, k = map(int, input().split())

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        weight, value = map(int, input().split())
        for j in range(1, k + 1):
            if j < weight:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
    print(dp[n][k])
