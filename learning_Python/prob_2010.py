import sys

def prob_2010():
    N = int(sys.stdin.readline())
    result = 1
    
    for _ in range(N):
        plug = int(sys.stdin.readline())
        result += plug - 1
    
    print(result)

prob_2010()