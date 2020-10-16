from itertools import combinations


def isIn(y, x):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False


def checkMap():
    for i in range(N):
        count = labMap[i].count(0)
        if count > 0:
            return False
    return True


def BFS(virusIdx):
    global requiredCnt

    queue = []
    # visited = [[False for _ in range(N)] for _ in range(N)]
    time = 0
    count = 0
    for vIdx in virusIdx:
        queue.append(virusList[vIdx])
        # visited[virusList[vIdx][0]][virusList[vIdx][1]] = True
        labMap[virusList[vIdx][0]][virusList[vIdx][1]] = 1

    while queue:
        # if checkMap():
        #     return time
        if count == requiredCnt:
            return time
        for _ in range(len(queue)):
            curr = queue.pop(0)
            for i in range(4):
                ny = curr[0] + pos[i][0]
                nx = curr[1] + pos[i][1]
                if isIn(ny, nx) and labMap[ny][nx] != 1:
                    if labMap[ny][nx] == 0:
                        count += 1
                    queue.append([ny, nx])
                    labMap[ny][nx] = 1
                    # visited[ny][nx] = True
        time += 1
    return N * N


def copyMap(orig, new):
    for i in range(N):
        for j in range(N):
            new[i][j] = orig[i][j]


def makeComb(now, goal, arr, prev):
    global minTime

    if now == goal:
        copyMap(tmpMap, labMap)
        minTime = min(minTime, BFS(arr[:]))
        return

    for i in range(prev + 1, len(virusIdx)):
        arr.append(virusIdx[i])
        makeComb(now + 1, goal, arr, i)
        arr.pop()


N, M = map(int, input().split())
labMap = [[int(x) for x in input().split()] for _ in range(N)]
tmpMap = [[0 for _ in range(N)] for _ in range(N)]

virusList = []
pos = [[-1, 0], [1, 0], [0, -1], [0, 1]]
minTime = N * N
requiredCnt = N * N

copyMap(labMap, tmpMap)

for i in range(N):
    for j in range(N):
        if labMap[i][j] == 2:
            virusList.append([i, j])
            requiredCnt -= 1
        elif labMap[i][j] == 1:
            requiredCnt -= 1

virusIdx = [int(x) for x in range(len(virusList))]
# makeComb(0, M, [], -1)
combList = list(combinations(virusIdx, M))

for comb in combList:
    copyMap(tmpMap, labMap)
    minTime = min(minTime, BFS(comb))

print(minTime if minTime < N * N else -1)
