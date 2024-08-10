"""
3kg 봉지와 5kg 봉지가 있다.
정확히 N kg 배달 해야 하는데, 최대한 적은 개수의 봉지를 들고 가야 한다.
정확히 N kg를 만들 수 없다면 -1 출력


1. 3kg 봉지로 처리 하는데, 5의 배수가 남도록.
"""


def sugar_deliver(weight) -> int:
    for x in range(weight):
        if (y := (weight - 3 * x) / 5).is_integer() and y >= 0:
            return int(y + x)
    return -1


print(sugar_deliver(int(input())))
