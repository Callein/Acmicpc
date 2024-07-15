# # nCm , 시간초과
# import itertools
# for i in range(int(input())):
#     n,m=map(int,input().split())
#     print(len(list(itertools.combinations(range(m),n))))

## 성공
from math import factorial as f
for i in range(int(input())):
    n,m=map(int,input().split())
    print(f(m)//(f(m-n)*f(n)))

# 더 짧은 거. 
# open(0) 에 관한 설명 
# https://stackoverflow.com/questions/53898231/integer-file-descriptor-0-in-open
import math
for i in[*open(0)][1:]:print(math.comb(int(i[2:]),int(i[:2])))

"""
for i in[*open(0)][1:]: 은 입력 파일을 열고, 파일 내용을 한 줄씩 읽어어는 루프 설정 (stdin)
open(0)은 스크립트가 실행 중인 현재 스크립트 파일을 열어서 파일 핸들을 반환합니다. 
[*open(0)]은 파일 내용을 리스트로 변환하고, [1:]는 첫 번째 줄을 제외하고 나머지 줄들을 선택합니다. 
따라서 이 루프는 입력 파일의 두 번째 줄부터 끝까지의 각 줄을 순회합니다.

print(math.comb(int(i[2:]), int(i[:2]))): 현재 줄에 있는 데이터를 가지고 수학적인 조합을 계산하고 결과를 출력합니다.

i[2:]는 현재 줄의 세 번째 문자부터 끝까지의 부분 문자열을 가져옵니다. 이 부분 문자열은 뒤의 숫자를 나타냅니다.
i[:2]는 현재 줄의 처음 두 문자를 가져옵니다. 이 부분 문자열은 앞의 숫자를 나타냅니다.
int(i[2:])와 int(i[:2])를 사용하여 이 문자열을 정수로 변환합니다.
math.comb 함수는 주어진 두 정수의 조합을 계산하는 함수입니다. 
즉, 두 정수를 이용하여 조합을 계산하고, 그 결과를 print 함수를 사용하여 출력합니다.

"""