"""
병합 정렬
근데 조건을 곁들인
"""
n = 0
numbers = []
temp = []
count = 0


def input_test_case():
    global n, numbers, temp, count

    n = int(input().strip())
    numbers = list(map(int, input().split()))
    # 매 테케마다 크기 n의 임시 배열 1개만 만들어 두고 재사용
    temp = [0] * n
    count = 0


def merge_sort(left, right):
    global count, numbers, temp

    # 원소가 1개 이하인 구간은 정렬 및 카운트할 필요 없음
    if right - left <= 1:
        return

    # 중간점 분할
    mid = (left + right) // 2

    # 재귀 호출 (슬라이싱 없이 인덱스로만 분할)
    merge_sort(left, mid)
    merge_sort(mid, right)

    # 오른쪽 구간을 병합하기 전,
    # 왼쪽 구간의 마지막 원소가 오른쪽 구간의 마지막 원소보다 큰 경우 카운트
    if numbers[mid - 1] > numbers[right - 1]:
        count += 1

    # 투 포인터 병합
    i, j, k = left, mid, left

    while i < mid and j < right:
        if numbers[i] <= numbers[j]:
            temp[k] = numbers[i]
            i += 1
        else:
            temp[k] = numbers[j]
            j += 1
        k += 1

    while i < mid:
        temp[k] = numbers[i]
        i += 1
        k += 1

    while j < right:
        temp[k] = numbers[j]
        j += 1
        k += 1

    # 병합된 결과를 원본 배열에 원복
    for idx in range(left, right):
        numbers[idx] = temp[idx]


def prob_5204():
    T = int(input().strip())

    for tc in range(1, T + 1):
        input_test_case()
        merge_sort(0, n)
        print(f"#{tc} {numbers[n // 2]} {count}")


if __name__ == "__main__":
    prob_5204()
