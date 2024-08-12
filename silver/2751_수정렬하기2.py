import sys
import heapq

# heapq 이용한 heapsort (정답)
heap = []
N = int(sys.stdin.readline())
for _ in range(N):
    heapq.heappush(heap, int(sys.stdin.readline()))
for _ in range(N):
    print(heapq.heappop(heap))

"""
join 시에 리스트의 각각 요소들은 str 이어야 한다. 그래서 str 로 받고 아스키 순서대로 되겠지 했는데 아니었다.
[반례]
==========
<input>
3
-1
-10
-2

<output>
-1
-10
-2
==========
=> 아스키 코드(ASCII)는 7비트 또는 8비트의 이진수로 문자를 표현하는 표준으로, 
0부터 127까지의 양의 정수로 모든 문자를 나타냅니다. 아스키 코드에서는 음수 정수가 존재하지 않음.
"""
# 오답
# print("\n".join(sorted([str(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))])))

# 정답
print("\n".join(map(str, sorted([int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]))))
