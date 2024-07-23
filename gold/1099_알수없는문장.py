# from itertools import permutations
# from collections import defaultdict
import sys


def calculate_cost(word, perm):
    return sum(1 for x, y in zip(word, perm) if x != y)


def solve(sentence, words):
    n = len(sentence)
    # word_perm = defaultdict(list)

    # # 각 단어의 모든 순열과 그 순열의 비용을 계산
    # for word in words:
    #     perms = set(permutations(word))
    #     for perm in perms:
    #         perm_str = ''.join(perm)
    #         cost = calculate_cost(word, perm_str)
    #         word_perm[word].append((perm_str, cost))

    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    # 문장의 각 substring 을 순회 하며 최소 비용 계산
    for i in range(n):
        if dp[i] == float('inf'):
            continue

        for word in words:
            len_word = len(word)
            if i + len_word <= n:
                substr = sentence[i:i + len_word]
                if sorted(substr) == sorted(word):
                    cost = calculate_cost(word, substr)
                    dp[i + len_word] = min(dp[i + len_word], dp[i] + cost)

    return dp[n] if dp[n] != float('inf') else -1


sentence = sys.stdin.readline().strip()
N = int(sys.stdin.readline().strip())
words = [sys.stdin.readline().strip() for _ in range(N)]


result = solve(sentence, words)
print(result)
