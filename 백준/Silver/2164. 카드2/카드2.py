import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

cards = deque([i+1 for i in range(N)])

while len(cards) != 1:
    cards.popleft()
    first = cards[0]
    cards.popleft()
    cards.append(first)

print(cards[0])
