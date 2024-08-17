"""
D: n을 두배로. 결과가 9999보다 큰 경우에는 10000으로 나눈 나머지를 취함 (2n mod 10000) 저장.
S: n에서 1을 뺀 결과를 저장. n이 0이라면 9999가 저장.
L: 각 자릿수를 왼편으로 회전시켜 저장. d2, d3, d4, d1 을 저장.
R: 각 자릿수를 오른편으로 회전시켜 저장. d4, d1, d2, d3 을 저장.



"""

import sys
from collections import deque

input_line = sys.stdin.readline
data = [list(map(int,input_line().split())) for _ in range(int(input_line()))]


def exec_d(n):
    return 2 * n % 10000

def exec_s(n):
    return (n - 1) % 10000

def exec_l(n):
    return n // 1000 + (n % 1000) * 10

def exec_r(n):
    return n // 10 + (n % 10) * 1000


for A, B in data:
    visited = [False for _ in range(10001)]
    deq = deque()
    deq.append((A, ''))
    visited[A] = True

    while deq:
        num, operation = deq.popleft()
        if num == B:
            print(operation)
            break

        if not visited[(d := exec_d(num))]:
            visited[d] = True
            deq.append((d, operation + 'D'))

        if not visited[(s := exec_s(num))]:
            visited[s] = True
            deq.append((s, operation + 'S'))

        if not visited[(l := exec_l(num))]:
            visited[l] = True
            deq.append((l, operation + 'L'))

        if not visited[(r := exec_r(num))]:
            visited[r] = True
            deq.append((r, operation + 'R'))
