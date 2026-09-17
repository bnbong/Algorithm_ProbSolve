n = 0
numbers = []


def input_test_case():
    global n, numbers

    n = int(input().strip())
    numbers = list(map(int, input().split()))


def special_sort():
    global n, numbers

    # 오름차순으로 우선 정렬
    numbers.sort()

    result = []
    left = 0
    right = n - 1

    # 큰 값(right), 작은 값(left)을 교대로 가져와 재배치
    while left <= right:
        result.append(numbers[right])
        right -= 1

        if left <= right:
            result.append(numbers[left])
            left += 1

    # 상위 10개만 슬라이싱하여 원본 배열에 갱신
    numbers = result[:10]


def prob_4843():
    T = int(input().strip())

    for tc in range(1, T + 1):
        input_test_case()
        special_sort()

        # 상위 10개 원소 출력
        ans = " ".join(map(str, numbers))
        print(f"#{tc} {ans}")


if __name__ == '__main__':
    prob_4843()