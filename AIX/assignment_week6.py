"""
1. a = [1,3,5,7,9,10]일 때 for문을 사용해 a = [4,6,8,10,12,13]으로 바꾸어 출력하는 프로그램을 작성하시오
(hint: a를 배열로 선언해주고 for i in a: 형식이나 for i in range(len(a)):를 활용해 기본적인 반복 루프를 만들고 배열에 인덱스로 접근해서 연산할 것)
2. while문과 if 를 사용하여, 31 이하의 양의 정수 중 짝수들의 합을 출력하는 프로그램을 작성하시오. (hint: 사전학습 슬라이드 8번의 코드를 활용할 것)
3. 이중 For문을 사용하는 아래의 코드를 완성하여 그 하단의 결과를 출력하는 프로그램을 작성하시오.
(코드의 4번째 줄 print() 함수의 end=’‘ 부분은 문장의 줄바꿈을 방지해 주고, 5번째 줄 print(“”) 는 줄바꿈을 위해 사용됨)
1
12
123
1234
12345
"""


def problem1():
    a = [1, 3, 5, 7, 9, 10]
    print("원래 배열:", a)

    for i in range(len(a)):
        a[i] = a[i] + 3

    print("변경된 배열:", a)
    return a


def problem2():
    total = 0
    num = 1

    while num <= 31:
        if num % 2 == 0:
            total += num
        num += 1

    print("31 이하의 양의 정수 중 짝수들의 합:", total)
    return total


def problem3():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end="")
        print("")

    return "패턴 출력 완료"


if __name__ == "__main__":
    problem1()
    problem2()
    problem3()
