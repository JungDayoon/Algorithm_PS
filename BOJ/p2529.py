def solution(prev, now, goal, result):
    global maxNum
    global minNum
    if now == goal:
        resultNum = int(result)
        maxNum = max(resultNum, maxNum)
        minNum = min(resultNum, minNum)
        return

    for i in range(10):
        if prev == -1:
            result += str(num[i])
            visited[i] = True
            solution(num[i], now+1, goal, result)
            result = result[:-1]
            visited[i] = False
        else:
            now_sign = sign[now]
            if now_sign == "<":
                if not visited[i] and prev < num[i]:
                    result += str(num[i])
                    visited[i] = True
                    solution(num[i], now+1, goal, result)
                    result = result[:-1]
                    visited[i] = False
            else:
                if not visited[i] and prev > num[i]:
                    result += str(num[i])
                    visited[i] = True
                    solution(num[i], now+1, goal, result)
                    result = result[:-1]
                    visited[i] = False

k = int(input())
sign = [x for x in input().split()]
visited = [False for _ in range(10)]
num = [int(x) for x in range(10)]

maxNum = 0
minNum = 9876543210
solution(-1, -1, k, "")

print(str(maxNum).zfill(k+1))
print(str(minNum).zfill(k+1))
