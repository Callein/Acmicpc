connection = [[(2*i)%10000, (i-1)%10000, (i%1000)*10 + i//1000, (i%10)*1000 + i//10] for i in range(10000)]
connection_reverse = [([i//2, i//2+5000] if i%2 == 0 else []) + [(i+1)%10000, (i%10)*1000 + i//10, (i%1000)*10 + i//1000] for i in range(10000)]

def solve(A, B, connection, connection_reverse):
    visited = {A:''}
    visited_reverse = {B:''}
    que = [A]
    que_reverse = [B]
    for depth in range(1, 10000):
        newQue = []
        for num in que:
            D, S, L, R = connection[num]
            if D not in visited:
                newQue.append(D)
                visited[D] = visited[num] + 'D'
                if D in visited_reverse:
                    return visited[D] + visited_reverse[D]
            if S not in visited:
                newQue.append(S)
                visited[S] = visited[num] + 'S'
                if S in visited_reverse:
                    return visited[S] + visited_reverse[S]
            if L not in visited:
                newQue.append(L)
                visited[L] = visited[num] + 'L'
                if L in visited_reverse:
                    return visited[L] + visited_reverse[L]
            if R not in visited:
                newQue.append(R)
                visited[R] = visited[num] + 'R'
                if R in visited_reverse:
                    return visited[R] + visited_reverse[R]
        que = [num for num in newQue]

        newQue_reverse = []
        for num in que_reverse:
            if num%2 == 0:
                D1, D2, S, L, R = connection_reverse[num]
                if D1 not in visited_reverse:
                    newQue_reverse.append(D1)
                    visited_reverse[D1] = 'D' + visited_reverse[num]
                    if D1 in visited:
                        return visited[D1] + visited_reverse[D1]
                if D2 not in visited_reverse:
                    newQue_reverse.append(D2)
                    visited_reverse[D2] = 'D' + visited_reverse[num]
                    if D2 in visited:
                        return visited[D2] + visited_reverse[D2]
            else:
                S, L, R = connection_reverse[num]
            if S not in visited_reverse:
                newQue_reverse.append(S)
                visited_reverse[S] = 'S' + visited_reverse[num]
                if S in visited:
                        return visited[S] + visited_reverse[S]
            if L not in visited_reverse:
                newQue_reverse.append(L)
                visited_reverse[L] = 'L' + visited_reverse[num]
                if L in visited:
                        return visited[L] + visited_reverse[L]
            if R not in visited_reverse:
                newQue_reverse.append(R)
                visited_reverse[R] = 'R' + visited_reverse[num]
                if R in visited:
                        return visited[R] + visited_reverse[R]
        que_reverse = [num for num in newQue_reverse]



from sys import stdin
T = int(input())
for _ in range(T):
    A, B = map(int, stdin.readline().split())
    print(solve(A, B, connection, connection_reverse))
