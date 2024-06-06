from enum import Enum

class numtoword(Enum):
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9

def solution(s):
    answer = []
    answer_str = ""
    eng_word = ""
    
    for word in s:
        try:
            if eng_word != "":
                for num in numtoword:
                    if str(num.name) in eng_word:
                        answer.append(num.value)
                        eng_word = eng_word.lstrip(str(num.name))
            is_intable = int(word)
            answer.append(word)

        except:
            eng_word += word
            continue

    for num in numtoword:
        if str(num.name) in eng_word:
            answer.append(num.value)
            eng_word.lstrip(str(num.name))
    
    for converted in answer:
        answer_str += str(converted)
    answer_str = int(answer_str)
    return answer_str