# dp[i] = min(dp[i], dp[i-n]+1, dp[i/2]+1, dp[i/3]+1)

def solution(x, y, n):
    answer = -1
    
    dp = [float('inf') for _ in range(y+1)]
    dp[x] = 0
    
    for i in range(x, y+1):
        if i + n <= y:
            dp[i+n] = min(dp[i+n], dp[i]+1)
        if i * 2 <= y:
            dp[i*2] = min(dp[i*2], dp[i]+1)
        if i * 3 <= y:
            dp[i*3] = min(dp[i*3], dp[i]+1)
    
    if dp[y]!=float('inf'): 
        answer = dp[y]

    return answer