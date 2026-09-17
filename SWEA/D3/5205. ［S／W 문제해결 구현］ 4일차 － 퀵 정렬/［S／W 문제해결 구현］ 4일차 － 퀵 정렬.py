"""
퀵정렬 구현, N 정수 정렬해 리스트 A 에 넣고 A[N//2] 저장된 거 출력
"""


n = 0
number_list = []


def input_test_case():
    global number_list, n

    n = int(input().strip())
    number_list = list(map(int, input().split()))


def quick_sort(target_list: list):
    if len(target_list) <= 1:
        return target_list

    pivot = target_list[0]

    left_list = [a for a in target_list if a < pivot]
    equal_list = [x for x in target_list if x == pivot]
    right_list = [b for b in target_list if b > pivot]

    return quick_sort(left_list) + equal_list + quick_sort(right_list)


def prob_5205():
    T = int(input().strip())

    for tc in range(1, T+1):
        input_test_case()

        result = quick_sort(number_list)

        print(f"#{tc} {result[n//2]}")


if __name__ == '__main__':
    prob_5205()
