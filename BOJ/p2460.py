import sys

nowCnt = 0
passenger = []

for i in range(10):
    Out, In = map(int, input().split())
    nowCnt = nowCnt - Out +In
    passenger.append(nowCnt)

print(max(passenger))