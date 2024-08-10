"""
이미 가지고 있는 랜선을 잘라서 필요한 랜선의 개수를 충족 시켜야 한다.
이 때 자르는 랜선의 길이는 최대가 되게 해야 한다.
자른 랜선의 개수가 필요한 랜선의 개수 보다 많아도 된다.
기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다.
이 때 자르는 랜선의 길이를 도출 하시오.

그냥 1씩 줄여가면서 찾아도 되지만, 이진 탐색으로 찾는게 더 효율적이다.
"""


# 지정한 길이로 자르면 몇개를 만들 수 있는지 측정
def count_lan_cables(lan, length):
    count = 0
    for l in lan:
        count += l // length
    return count


def max_lan_cable_length(n, lan):
    left, right = 1, max(lan)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if count_lan_cables(lan, mid) >= n:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


k, n = map(int, input().split())
have = [int(input()) for _ in range(k)]

print(max_lan_cable_length(n, have))
