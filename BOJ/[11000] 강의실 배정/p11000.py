import heapq

N = int(input())
pq = []
classCnt = 0
classTime = [[int(x) for x in input().split()] for _ in range(N)]
classTime = sorted(classTime, key=lambda t: t[0])
for start, end in classTime:
    if len(pq) > 0:
        if pq[0] > start:
            heapq.heappush(pq, end)
            classCnt += 1
        else:
            heapq.heappop(pq)
            heapq.heappush(pq, end)
    else:
        heapq.heappush(pq, end)
        classCnt += 1

print(classCnt)

