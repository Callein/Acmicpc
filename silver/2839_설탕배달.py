"""
3kg 봉지와 5kg 봉지가 있다.
정확히 N kg 배달 해야 하는데, 최대한 적은 개수의 봉지를 들고 가야 한다.
정확히 N kg를 만들 수 없다면 -1 출력


• 3kg 봉지로 처리 하는데, 5의 배수가 남도록 해야 한다.
• weight = 3x + 5y 이다. 이 때  y가 최대가 되게 해야 하므로,
  y = (weight - 3 * x) / 5) , x : 0 ~ (weight//3+1) -1
  에서 y 가 처음으로 양의 정수가 되는 지점이 y가 최대인 지점이다.
• for 문이 다 돌기 이전에 무조건 y는 양의 정수가 될 수밖에 없다. (y = 0도 return 조건에 부합)
• 만약 for 문이 다 돌면 weight 는 정확히 N kg를 만들 수 없었던 것이다. ( return -1 )
"""


def sugar_deliver(weight) -> int:
    for x in range(weight//3+1):
        if (y := (weight - 3 * x) / 5).is_integer() and y >= 0:
            return int(y + x)
    return -1


print(sugar_deliver(int(input())))
