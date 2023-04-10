import heapq, sys


N = int(input())
maxheap = []
minheap = []

for _ in range(N):
    number = int(sys.stdin.readline())

    if len(maxheap) == len(minheap):
        heapq.heappush(maxheap, -number)
    else:
        heapq.heappush(minheap, number)

    if len(maxheap) >= 1 and len(minheap) >= 1 and maxheap[0] * -1 > minheap[0]:
        maxheap_number = heapq.heappop(maxheap) * -1
        minheap_numebr = heapq.heappop(minheap)

        heapq.heappush(minheap, maxheap_number)
        heapq.heappush(maxheap, minheap_numebr * -1)

    print(maxheap[0] * -1)
