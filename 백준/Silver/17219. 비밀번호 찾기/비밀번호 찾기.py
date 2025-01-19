import sys

N, M = map(int, sys.stdin.readline().split())

pw_list = dict()

for _ in range(N):
    url, pw = map(str, sys.stdin.readline().strip().split())
    pw_list[url] = pw

for _ in range(M):
    target_url = str(sys.stdin.readline().strip())
    print(pw_list[target_url])
