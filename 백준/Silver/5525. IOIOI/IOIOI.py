import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def kmp(string: str, pattern: str):
    table = [0 for _ in range(len(pattern))]
    i = 0

    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i-1]

        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i

    result = []

    i = 0
    for j in range(len(string)):
        while i > 0 and pattern[i] != string[j]:
            i = table[i-1]

        if pattern[i] == string[j]:
            i += 1
            if i == len(pattern):
                result.append(j - i + 1)
                i = table[i-1]

    return result


N = int(input())
M = int(input())
S = str(input())

pattern = "I" + "OI"*N

print(len(kmp(S, pattern)))
