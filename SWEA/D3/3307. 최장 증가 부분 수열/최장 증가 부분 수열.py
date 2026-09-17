"""
최장 증가 부분 수열의 길이
"""


N = 0
numbers = []


def input_test_case():
    global N, numbers

    N = int(input().strip())
    numbers = list(map(int, input().split()))


def prob_3307():
    T = int(input().strip())

    for tc in range(1, T+1):
        input_test_case()

        # dp[i] : numbers[i]를 마지막 원소로 갖는 최장 증가 부분 수열의 길이
        dp = [1] * N

        # LIS DP 점화식
        for i in range(N):
            for j in range(i):
                # 이전 원소(j)가 현재 원소(i)보다 작으면 LIS 길이 갱신
                if numbers[j] < numbers[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # 구한 길이 중 최댓값 출력
        max_length = max(dp)
        print(f"#{tc} {max_length}")


if __name__ == '__main__':
    prob_3307()
