def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    used = []
    
    i = 0
    j = len(people) - 1

    while len(people) != 0 and i <= j:

        a = people[i]
        b = people[j]


        if a + b <= limit and j != 0:
            used.append((a, b))
            i += 1
            j -= 1
            continue
        else:
            used.append((a))
            i += 1
            continue

    print(used)

    answer = len(used)

    return answer