# 풀이 : (a + 1) * (b + 1) * (c + 1) ... - 1
T = int(input())

for t in range(T):
    N = int(input())
    gadget = dict()
    for n in range(N):
        cloth, place = map(str, input().split())
        if place in gadget:
            gadget[place].append(cloth)
        else:
            gadget[place] = [cloth]
    results = [0] * len(gadget.keys())
    i = 0
    for key in gadget.keys():
        results[i] = len(gadget[key])
        i += 1
    result = 1
    for i in range(len(results)):
        result *= (results[i]+1)
    print(result - 1)
