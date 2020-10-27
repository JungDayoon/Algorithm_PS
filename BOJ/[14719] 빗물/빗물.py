H, W = map(int, input().split())
rain = [int(x) for x in input().split()]
result = [0 for _ in range(W)]


for rIdx in range(1, len(rain)-1):
    rItem = rain[rIdx]
    leftMax = max(rain[0: rIdx])
    rightMax = max(rain[rIdx:W])
    result[rIdx] = min(leftMax, rightMax)

rainSum = 0
for i in range(W):
    nowRain = (result[i] - rain[i] if result[i] - rain[i] > 0 else 0)
    rainSum += nowRain

print(rainSum)



