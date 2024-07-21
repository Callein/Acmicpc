# N% 절사 평균의 경우 위와 아래 에서 N/2% 를 각각 제외 하고 평균을 계산.
# 모든 계산 결과는 반올림 한다.


# 원형
num = int(input())
tm = int(round(num/100*15, 0))
rank = sorted([int(input()) for _ in range(num)])[tm:num-tm]
ret = int(round(sum(rank)/(num-2*tm), 0))
print(tm, rank, ret)


# 줄여서 썼지만, Python 의 round() 는 사사 오입 (홀수는 올림, 짝수는 내림) 법칙에 의해 오답을 낼 수 있음
tm = int(round((n := int(input()))/100*15, 0))
print(0 if n == 0 else int(round(sum(sorted([int(input()) for _ in range(n)])[tm:n-tm])/(n-2*tm), 0)))


# 0.5를 더한 뒤 int() 로 소수점 이하를 모두 버려 주면 반올림 효과를 얻을 수 있음
tm = int((n := int(input())) / 100 * 15 + 0.5)
print(0 if n == 0 else int(sum(sorted([int(input()) for _ in range(n)])[tm:n-tm]) / (n - 2 * tm) + 0.5))


# one-liner 뇌절편
print(0 if (n := int(input())) == 0 else (lambda t: int(sum(sorted([int(input()) for _ in range(n)])[t:n-t]) / (n - 2 * t) + 0.5))(int(n / 100 * 15 + 0.5)))
