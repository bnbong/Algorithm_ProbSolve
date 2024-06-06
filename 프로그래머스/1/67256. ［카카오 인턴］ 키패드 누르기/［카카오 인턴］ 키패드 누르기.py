def check(number, keypad, left_idx, right_idx, hand):
    for i in range(4):
        for j in range(3):
            if keypad[i][j] == number:
                if int(number) in (1, 4, 7):
                    answer = 'L'
                    left_idx = [i, j]
                    return answer, left_idx, right_idx
                elif int(number) in (3, 6, 9):
                    answer = 'R'
                    right_idx = [i, j]
                    return answer, left_idx, right_idx
                elif int(number) in (2, 5, 8, 0):
                    distance_left = abs(int(left_idx[0]) - i) + abs(int(left_idx[1]) - j)
                    distance_right = abs(int(right_idx[0]) - i) + abs(int(right_idx[1]) - j)
                    if distance_left > distance_right:
                        right_idx = [i, j]
                        answer = 'R'
                        return answer, left_idx, right_idx
                    elif distance_left < distance_right:
                        left_idx = [i, j]
                        answer = 'L'
                        return answer, left_idx, right_idx
                    elif distance_left == distance_right:
                        if hand == "right":
                            right_idx = [i, j]
                            answer = 'R'
                            return answer, left_idx, right_idx
                        else:
                            left_idx = [i, j]
                            answer = 'L'
                            return answer, left_idx, right_idx

def solution(numbers, hand):
    answer = ''
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    left = '*'
    left_idx = [3,0]
    right = '#'
    right_idx = [3,2]
    for number in numbers:
        answer_char, left_idx, right_idx = check(number, keypad, left_idx, right_idx, hand)
        answer += answer_char
            
    return answer