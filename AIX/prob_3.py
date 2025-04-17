"""
- 수학 점수에 대한 변수를 선언하고 95를 대입

- 점수가 90점이 넘으면 “Excellent”를 출력

- 점수가 90점 이하이면서 80점을 넘으면 “Good”을 출력

- 위의 모든 조건을 만족하지 못하면 “satisfactory”를 출력
"""

score: int = 95

if score > 90:
    print("Excellent")
elif 80 < score <= 90:
    print("Good")
else:
    print("satisfactory")
