import sys

N = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
print(sum(n/max(data)*100 for n in data)/N)